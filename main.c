#include <pthread.h>

#include "board.h"
#include "cli.h"
#include "swsys.h"
#include "xml_inline.h"

swsys_t core_sys;
int catpilot(void);

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
