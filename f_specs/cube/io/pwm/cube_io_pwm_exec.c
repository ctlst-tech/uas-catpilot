#include "cube_io_pwm.h"
#include "board.h"

fspec_rv_t cube_io_pwm_pre_exec_init(
        const cube_io_pwm_optional_inputs_flags_t *input_flags,
        const cube_io_pwm_params_t *p,
        cube_io_pwm_state_t *state
) {

    cubeio_set_freq(cubeio, 0xFFFF, 400);
    cubeio_set_range(cubeio, CUBEIO_PWM, 0, p->ch1_bipolar ? CUBEIO_CHANNEL_BIPOLAR : CUBEIO_CHANNEL_UNIPOLAR, p->ch1_min, p->ch1_max);
    cubeio_set_range(cubeio, CUBEIO_PWM, 1, p->ch2_bipolar ? CUBEIO_CHANNEL_BIPOLAR : CUBEIO_CHANNEL_UNIPOLAR, p->ch2_min, p->ch2_max);
    cubeio_set_range(cubeio, CUBEIO_PWM, 2, p->ch3_bipolar ? CUBEIO_CHANNEL_BIPOLAR : CUBEIO_CHANNEL_UNIPOLAR, p->ch3_min, p->ch3_max);
    cubeio_set_range(cubeio, CUBEIO_PWM, 3, p->ch4_bipolar ? CUBEIO_CHANNEL_BIPOLAR : CUBEIO_CHANNEL_UNIPOLAR, p->ch4_min, p->ch4_max);
    cubeio_set_range(cubeio, CUBEIO_PWM, 4, p->ch5_bipolar ? CUBEIO_CHANNEL_BIPOLAR : CUBEIO_CHANNEL_UNIPOLAR, p->ch5_min, p->ch5_max);
    cubeio_set_range(cubeio, CUBEIO_PWM, 5, p->ch6_bipolar ? CUBEIO_CHANNEL_BIPOLAR : CUBEIO_CHANNEL_UNIPOLAR, p->ch6_min, p->ch6_max);
    cubeio_set_range(cubeio, CUBEIO_PWM, 6, p->ch7_bipolar ? CUBEIO_CHANNEL_BIPOLAR : CUBEIO_CHANNEL_UNIPOLAR, p->ch7_min, p->ch7_max);
    cubeio_set_range(cubeio, CUBEIO_PWM, 7, p->ch8_bipolar ? CUBEIO_CHANNEL_BIPOLAR : CUBEIO_CHANNEL_UNIPOLAR, p->ch8_min, p->ch8_max);
    state->inited = TRUE;

    return fspec_rv_ok;
}

void cube_io_pwm_exec(const cube_io_pwm_inputs_t *i, const cube_io_pwm_params_t *p, cube_io_pwm_state_t *state){
    double pwm[16];

    gpio_set(&gpio_fmu_pwm[1]);

    if(i->arm && !state->arm_passed) {
        cubeio_force_safety_off(cubeio);
        state->arm_passed = TRUE;
        state->disarm_passed = FALSE;
    } else if (!i->arm && !state->disarm_passed){
        cubeio_force_safety_on(cubeio);
        state->arm_passed = FALSE;
        state->disarm_passed = TRUE;
    }

    pwm[0] = i->ch1;
    pwm[1] = i->ch2;
    pwm[2] = i->ch3;
    pwm[3] = i->ch4;
    pwm[4] = i->ch5;
    pwm[5] = i->ch6;
    pwm[6] = i->ch7;
    pwm[7] = i->ch8;

    cubeio_set_pwm(cubeio, 8, pwm);

    // For debug reset pin in CubeIO thread
    // gpio_reset(&gpio_fmu_pwm[1]);
}
