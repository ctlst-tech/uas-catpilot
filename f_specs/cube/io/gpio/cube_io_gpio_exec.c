#include "cube_io_gpio.h"
#include "board.h"

void cube_io_gpio_exec(const cube_io_gpio_inputs_t *i, cube_io_gpio_outputs_t *o, const cube_io_gpio_params_t *p)
{
    if(p->channel < 1 || p->channel > 6) return;

    if(i->optional_inputs_flags.input_bool) {
        gpio_set_state(&gpio_fmu_pwm[p->channel - 1], i->input_bool);
    } if (i->optional_inputs_flags.input_float) {
        gpio_set_state(&gpio_fmu_pwm[p->channel - 1],
                      i->input_float > 0.5 ? 1 : 0);
    } else {
        gpio_toggle(&gpio_fmu_pwm[p->channel - 1]);
    }
}

void test_gpio5_set() {
    gpio_set_state(&gpio_fmu_pwm[5], 1);
}

void test_gpio5_clear() {
    gpio_set_state(&gpio_fmu_pwm[5], 0);
}

