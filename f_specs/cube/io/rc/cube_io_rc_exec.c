#include "cube_io_rc.h"
#include "board.h"

fspec_rv_t cube_io_rc_pre_exec_init() {

    cubeio_set_range(cubeio, CUBEIO_RC, 0, CUBEIO_CHANNEL_BIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 1, CUBEIO_CHANNEL_BIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 2, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 3, CUBEIO_CHANNEL_BIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 4, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 5, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 6, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 7, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 8, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 9, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 9, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 10, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 11, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 12, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 13, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 14, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);
    cubeio_set_range(cubeio, CUBEIO_RC, 15, CUBEIO_CHANNEL_UNIPOLAR, 982, 2006);

    return fspec_rv_ok;
}


void cube_io_rc_exec(cube_io_rc_outputs_t *o)
{
    double rc[16];

    gpio_set(&gpio_fmu_pwm[2]);

    cubeio_get_rc(cubeio, rc);
    o->rc_channel1 = rc[0];
    o->rc_channel2 = rc[1];
    o->rc_channel3 = rc[2];
    o->rc_channel4 = rc[3];
    o->rc_channel5 = rc[4];
    o->rc_channel6 = rc[5];
    o->rc_channel7 = rc[6];
    o->rc_channel8 = rc[7];
    o->rc_channel9 = rc[8];
    o->rc_channel10 = rc[9];
    o->rc_channel11 = rc[10];
    o->rc_channel12 = rc[11];
    o->rc_channel13 = rc[12];
    o->rc_channel14 = rc[13];
    o->rc_channel15 = rc[14];
    o->rc_channel16 = rc[15];

    // For debug reset pin in CubeIO thread
    // gpio_reset(&gpio_fmu_pwm[2]);
}
