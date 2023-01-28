#include <pthread.h>

#include "board.h"
#include "cli.h"
#include "swsys.h"
#include "xml_inline.h"

swsys_t core_sys;
void *catpilot(void *param);

// TODO: replace to c-atom
#include "swsys.h"
static char swsys_cmd[CLI_MAX_CMD_LENGTH];
static char *swsys_cmd_offset;

int swsys_commander(int argc, char **argv) {
    if (argc < 3) {
        printf("Usage: swsys [task] func_name=[func] [param_alias]=[value]\n");
        return 0;
    }

    swsys_cmd_offset = swsys_cmd;
    for (int i = 2; i < argc; i++) {
        if (swsys_cmd_offset > swsys_cmd + CLI_MAX_CMD_LENGTH) {
            printf("Command exceeds max length\n");
            return 0;
        }
        strncpy(swsys_cmd_offset, argv[i],
                swsys_cmd + CLI_MAX_CMD_LENGTH - swsys_cmd_offset);
        swsys_cmd_offset += strnlen(argv[i], CLI_MAX_CMD_LENGTH);
        swsys_cmd_offset[0] = ' ';
        swsys_cmd_offset++;
    }

    swsys_rv_t rv = swsys_set_params(&core_sys, argv[1], swsys_cmd);

    if (rv != swsys_e_ok) {
        printf("Wrong command\n");
        printf("Usage: swsys [task] func_name=[func] [param_alias]=[value]\n");
    } else {
        printf("Command accepted\n");
    }

    return 0;
}

int main(void) {
    board_start(catpilot, 16 * 1024);
    while (1) {
    }
}

void *catpilot(void *param) {
    pthread_setname_np((char *)__func__);

    board_init(CLI_PORT, CLI_BAUDRATE);

#ifdef MAINTENANCE_MODE
    board_debug_mode();
#else
    xml_inline_mount("/cfg");
    cli_cmd_reg("swsys", swsys_commander);

    swsys_rv_t swsys_rv = swsys_load("/cfg/swsys.xml", "/cfg", &core_sys);
    if (swsys_rv == swsys_e_ok) {
        LOG_INFO("SYSTEM", "Configuration loading successful");
        swsys_rv = swsys_top_module_start(&core_sys);
        if (swsys_rv != swsys_e_ok) {
            LOG_ERROR("SYSTEM", "Module start error");
        }
    } else {
        LOG_ERROR("SYSTEM", "Configuration loading error");
    }
#endif

    board_fail();

    return NULL;
}
