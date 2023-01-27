#include <pthread.h>

#include "board.h"
#include "swsys.h"
#include "xml_inline.h"

swsys_t core_sys;
void *catpilot(void *param);

int main(void) {
    board_start(catpilot, 16*1024);
    while (1) {
    }
}

void *catpilot(void *param) {
    pthread_setname_np((char *)__func__);

    board_init(CLI_PORT, CLI_BAUDRATE);

#ifdef DEBUG_MODE
    board_debug_mode();
#else
    xml_inline_mount("/cfg");

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
