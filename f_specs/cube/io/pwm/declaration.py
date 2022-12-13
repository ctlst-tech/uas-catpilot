from fspeclib import *

Function(
    name='cube.io.pwm',
    title=LocalizedString(
        en='io'
    ),
    has_pre_exec_init_call=True,
    parameters=[
        Parameter(
            name='ch1_min',
            title='Channel 1 minimum PWM',
            value_type='core.type.u32',
            default=700,
        ),
        Parameter(
            name='ch2_min',
            title='Channel 2 minimum PWM',
            value_type='core.type.u32',
            default=700,
        ),
        Parameter(
            name='ch3_min',
            title='Channel 3 minimum PWM',
            value_type='core.type.u32',
            default=700,
        ),
        Parameter(
            name='ch4_min',
            title='Channel 4 minimum PWM',
            value_type='core.type.u32',
            default=700,
        ),
        Parameter(
            name='ch5_min',
            title='Channel 5 minimum PWM',
            value_type='core.type.u32',
            default=700,
        ),
        Parameter(
            name='ch6_min',
            title='Channel 6 minimum PWM',
            value_type='core.type.u32',
            default=700,
        ),
        Parameter(
            name='ch7_min',
            title='Channel 7 minimum PWM',
            value_type='core.type.u32',
            default=700,
        ),
        Parameter(
            name='ch8_min',
            title='Channel  8 minimum PWM',
            value_type='core.type.u32',
            default=700,
        ),
        Parameter(
            name='ch1_max',
            title='Channel 1 maximum PWM',
            value_type='core.type.u32',
            default=2200,
        ),
        Parameter(
            name='ch2_max',
            title='Channel 2 maximum PWM',
            value_type='core.type.u32',
            default=2200,
        ),
        Parameter(
            name='ch3_max',
            title='Channel 3 maximum PWM',
            value_type='core.type.u32',
            default=2200,
        ),
        Parameter(
            name='ch4_max',
            title='Channel 4 maximum PWM',
            value_type='core.type.u32',
            default=2200,
        ),
        Parameter(
            name='ch5_max',
            title='Channel 5 maximum PWM',
            value_type='core.type.u32',
            default=2200,
        ),
        Parameter(
            name='ch6_max',
            title='Channel 6 maximum PWM',
            value_type='core.type.u32',
            default=2200,
        ),
        Parameter(
            name='ch7_max',
            title='Channel 7 maximum PWM',
            value_type='core.type.u32',
            default=2200,
        ),
        Parameter(
            name='ch8_max',
            title='Channel 8 maximum PWM',
            value_type='core.type.u32',
            default=2200,
        ),
        Parameter(
            name='ch1_bipolar',
            title='Channel 1 bipolar mode enable',
            value_type='core.type.bool',
            default='FALSE',
        ),
        Parameter(
            name='ch2_bipolar',
            title='Channel 2 bipolar mode enable',
            value_type='core.type.bool',
            default='FALSE',
        ),
        Parameter(
            name='ch3_bipolar',
            title='Channel 3 bipolar mode enable',
            value_type='core.type.bool',
            default='FALSE',
        ),
        Parameter(
            name='ch4_bipolar',
            title='Channel 4 bipolar mode enable',
            value_type='core.type.bool',
            default='FALSE',
        ),
        Parameter(
            name='ch5_bipolar',
            title='Channel 5 bipolar mode enable',
            value_type='core.type.bool',
            default='FALSE',
        ),
        Parameter(
            name='ch6_bipolar',
            title='Channel 6 bipolar mode enable',
            value_type='core.type.bool',
            default='FALSE',
        ),
        Parameter(
            name='ch7_bipolar',
            title='Channel 7 bipolar mode enable',
            value_type='core.type.bool',
            default='FALSE',
        ),
        Parameter(
            name='ch8_bipolar',
            title='Channel 8 bipolar mode enable',
            value_type='core.type.bool',
            default='FALSE',
        ),
    ],
    inputs=[
        Input(
            name='arm',
            title='Arming signal',
            description='CUBE IO PWM output arming signal',
            value_type='core.type.bool'
        ),
        Input(
            name='ch1',
            title='Channel 1 input',
            value_type='core.type.f64',
            mandatory=False
        ),
        Input(
            name='ch2',
            title='Channel 2 input',
            value_type='core.type.f64',
            mandatory=False
        ),
        Input(
            name='ch3',
            title='Channel 3 input',
            value_type='core.type.f64',
            mandatory=False
        ),
        Input(
            name='ch4',
            title='Channel 4 input',
            value_type='core.type.f64',
            mandatory=False
        ),
        Input(
            name='ch5',
            title='Channel 5 input',
            value_type='core.type.f64',
            mandatory=False
        ),
        Input(
            name='ch6',
            title='Channel 6 input',
            value_type='core.type.f64',
            mandatory=False
        ),
        Input(
            name='ch7',
            title='Channel 7 input',
            value_type='core.type.f64',
            mandatory=False
        ),
        Input(
            name='ch8',
            title='Channel 8 input',
            value_type='core.type.f64',
            mandatory=False
        ),
    ],
    outputs=[],
    state=[
        Variable(
            name='decimation_counter',
            title='Decimation counter',
            value_type='core.type.u32'
        ),
        Variable(
            name='inited',
            title='FIXME',
            value_type='core.type.bool'
        ),
        Variable(
            name='arm_passed',
            title='Arm passed event',
            value_type='core.type.bool'
        ),
        Variable(
            name='disarm_passed',
            title='Disarm passed event',
            value_type='core.type.bool'
        ),
    ],
    parameter_constraints=[],
)
