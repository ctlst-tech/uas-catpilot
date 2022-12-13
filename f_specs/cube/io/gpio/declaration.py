from fspeclib import *

Function(
    name='cube.io.gpio',
    title=LocalizedString(
        en='gpio'
    ),
    parameters=[
        Parameter(
            name='channel',
            title='channel',
            value_type='core.type.u8',
            tunable=True,
            default=0,
        )
    ],
    inputs=[
        Input(
            name='input_bool',
            title='input bool',
            value_type='core.type.bool',
            mandatory=False,
        ),
        Input(
            name='input_float',
            title='input float 64',
            value_type='core.type.f64',
            mandatory=False
        ),
    ],
    outputs=[
        Output(
            name='out',
            title='out',
            value_type='core.type.bool'
        ),
    ],
    state=[],
    parameter_constraints=[],
)
