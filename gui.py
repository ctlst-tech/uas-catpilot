#!/usr/bin/env python3

import sys

sys.path.append("./catpilot/c-atom/eswb/pytools")

from controls import *
from monitor import *
from eswbmon import *

mon_bus_name = 'monitor'
telemetry_dir_name = 'telemetry'

args_parser = ArgParser()
args = args_parser.args

mon = EswbMonitor(monitor_bus_name=mon_bus_name, argv=sys.argv)

mon.mkdir(telemetry_dir_name)

topics_root = mon_bus_name + '/' + telemetry_dir_name

mon.bridge_sdtl(path=args.serdev, baudrate=args.serbaud, bridge_to='telemetry')

# att_indicator = EwAttitudeIndicator([DataSourceEswbTopic('roll', path=f'{topics_root}/nav/nav/roll', mult=57.32),
#                                DataSourceEswbTopic('pitch', path=f'{topics_root}/nav/nav/pitch', mult=57.32)])

#
# ai = EwAttitudeIndicator([
#     DataSourceSinus('s1', iphase=0.0, mult=45),
#     DataSourceSinus('s2', iphase=1.0, mult=20)
# ])

ai = EwAttitudeIndicator([
    DataSourceEswbTopic('roll', path=f'{topics_root}/nav/nav/roll', mult=57.32),
    DataSourceEswbTopic('pitch', path=f'{topics_root}/nav/nav/pitch', mult=57.32)
])

hi = EwHeadingIndicator([DataSourceEswbTopic('yaw', path=f'{topics_root}/nav/nav/yaw', mult=57.32)])

compass = EwHeadingIndicator([DataSourceEswbTopic('azimuth', path=f'{topics_root}/nav/nav/azimuth', mult=57.32)])

imu_roll_pitch = EwChart([DataSourceEswbTopic('roll', path=f'{topics_root}/nav/nav/roll', mult=57.32),
                        DataSourceEswbTopic('pitch', path=f'{topics_root}/nav/nav/pitch', mult=57.32)],
                        data_range=(-60, +60))

imu_omega = EwChart([DataSourceEswbTopic('omega_x', path=f'{topics_root}/nav/nav/omega/x', mult=57.32),
                        DataSourceEswbTopic('omega_y', path=f'{topics_root}/nav/nav/omega/y', mult=57.32),
                        DataSourceEswbTopic('omega_z', path=f'{topics_root}/nav/nav/omega/z', mult=57.32)],
                        data_range=(-60, +60))

imu_a = EwChart([DataSourceEswbTopic('a_x', path=f'{topics_root}/nav/nav/a/x'),
                        DataSourceEswbTopic('a_y', path=f'{topics_root}/nav/nav/a/y'),
                        DataSourceEswbTopic('a_z', path=f'{topics_root}/nav/nav/a/z')],
                        data_range=(-15, +15))

mag = EwChart([DataSourceEswbTopic('mag_x', path=f'{topics_root}/nav/nav/induction/x'),
                        DataSourceEswbTopic('mag_y', path=f'{topics_root}/nav/nav/induction/y'),
                        DataSourceEswbTopic('mag_z', path=f'{topics_root}/nav/nav/induction/z'),
                        DataSourceEswbTopic('mag', path=f'{topics_root}/nav/nav/ind_magnitude')],
                        data_range=(-0.7, +0.7))

hk_sine = EwChart([DataSourceEswbTopic('sine', path=f'{topics_root}/hk/sine'),
                        # DataSourceSinus('s1', iphase=0.0),
                        # DataSourceSinus('s2', iphase=1.0)
                   ],
                        data_range=(-1, +1))

manc_xy = EwCursor([(DataSourceEswbTopic('x', path=f'{topics_root}/cont/man_cont/direct/x'),
                          DataSourceEswbTopic('y', path=f'{topics_root}/cont/man_cont/direct/y'))])

mon.add_widget(EwGroup([ai, hi, compass, imu_roll_pitch, ]))
mon.add_widget(EwGroup([manc_xy, imu_omega, imu_a, mag, hk_sine]))

mon.add_widget(mon.get_stat_widget())
mon.run()
