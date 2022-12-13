from fspeclib import *

Function(
    name='cube.sensors.icm20948',
    title=LocalizedString(
        en='icm20948'
    ),
    parameters=[],
    inputs=[],
    outputs=[
        Output(
            name='ax',
            title='X-axis acceleration',
            value_type='core.type.f64'
        ),
        Output(
            name='ay',
            title='Y-axis acceleration',
            value_type='core.type.f64'
        ),
        Output(
            name='az',
            title='Z-axis acceleration',
            value_type='core.type.f64'
        ),
        Output(
            name='wx',
            title='X-axis angular rate',
            value_type='core.type.f64'
        ),
        Output(
            name='wy',
            title='Y-axis angular rate',
            value_type='core.type.f64'
        ),
        Output(
            name='wz',
            title='Z-axis angular rate',
            value_type='core.type.f64'
        ),
    ],
    state=[],
    parameter_constraints=[]
)
