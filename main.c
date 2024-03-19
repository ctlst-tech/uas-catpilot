#include <pthread.h>

#include "board.h"
#include "cli.h"
#include "swsys.h"
#include "xml_inline.h"

swsys_t core_sys;
int catpilot(void);

#define SWSYS_COMMANDER_MAX_CMD_LENGTH 128
static char swsys_cmd[SWSYS_COMMANDER_MAX_CMD_LENGTH];
static char *swsys_cmd_offset;
static swsys_t *swsys_commander_ptr;

swsys_rv_t swsys_commander_init(swsys_t *swsys) {
    if (swsys != NULL) {
        swsys_commander_ptr = swsys;
        return swsys_e_ok;
    }
    return swsys_e_invargs;
}

int swsys_commander(int argc, char **argv) {
    if (argc < 3) {
        dbg_msg("Usage: swsys [task] func_name=[func] [param_alias]=[value]");
        return 0;
    }

    if (swsys_commander_ptr == NULL) {
        dbg_msg("swsys_commander is not initialized");
        return 0;
    }

    swsys_cmd_offset = swsys_cmd;
    for (int i = 2; i < argc; i++) {
        if (swsys_cmd_offset > swsys_cmd + SWSYS_COMMANDER_MAX_CMD_LENGTH) {
            dbg_msg("Command exceeds max length");
            return 0;
        }
        strncpy(swsys_cmd_offset, argv[i],
                swsys_cmd + SWSYS_COMMANDER_MAX_CMD_LENGTH - swsys_cmd_offset);
        swsys_cmd_offset += strnlen(argv[i], SWSYS_COMMANDER_MAX_CMD_LENGTH);
        swsys_cmd_offset[0] = ' ';
        swsys_cmd_offset++;
    }

    swsys_rv_t rv = swsys_set_params(swsys_commander_ptr, argv[1], swsys_cmd);

    if (rv != swsys_e_ok) {
        dbg_msg("Wrong command");
        dbg_msg("Usage: swsys [task] func_name=[func] [param_alias]=[value]");
    } else {
        dbg_msg("Command accepted");
    }

    return 0;
}

int main(void) {
    board_start(catpilot, 8192, CLI_PORT, CLI_BAUDRATE);
    while (1) {
    }
}

int catpilot(void) {
    pthread_setname_np((char *)__func__);
    xml_inline_mount("/cfg");
    cli_cmd_reg("swsys", swsys_commander);
    swsys_rv_t swsys_rv = swsys_load("/cfg/swsys.xml", "/cfg", &core_sys);
    swsys_rv_t swsys_cmd_rv = swsys_commander_init(&core_sys);
    if (swsys_rv == swsys_e_ok && swsys_cmd_rv == swsys_e_ok) {
        printf("SWSYS \"%s\" loaded\n",
               core_sys.name != NULL ? core_sys.name : "no name");
        LOG_INFO("SYSTEM", "Configuration loading successful");
        swsys_rv = swsys_top_module_start(&core_sys);
        if (swsys_rv != swsys_e_ok) {
            LOG_ERROR("SYSTEM", "Module start error");
            printf("SWSYS \"%s\" failed to start\n",
                   core_sys.name != NULL ? core_sys.name : "no name");
        }
    } else {
        LOG_ERROR("SYSTEM", "Configuration loading error");
    }
    return -1;
}
