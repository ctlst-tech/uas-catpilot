#!/usr/bin/env python3

import sys

sys.path.append("./catpilot/c-atom/eswb/pytools")

from eswbmon import *

mon_bus_name = 'monitor'
telemetry_dir_name = 'telemetry'

args_parser = ArgParser()
args = args_parser.args

mon = Monitor(monitor_bus_name=mon_bus_name, argv=sys.argv)

mon.mkdir(telemetry_dir_name)

topics_root = mon_bus_name + '/' + telemetry_dir_name

mon.bridge_sdtl(path=args.serdev, baudrate=args.serbaud, bridge_to='telemetry')

imu_roll_pitch = ewChart([DataSourceEswbTopic('roll', path=f'{topics_root}/nav/nav/roll', mult=57.32),
                        DataSourceEswbTopic('pitch', path=f'{topics_root}/nav/nav/pitch', mult=57.32)],
                        data_range=(-60, +60))

imu_omega = ewChart([DataSourceEswbTopic('omega_x', path=f'{topics_root}/nav/nav/omega/x', mult=57.32),
                        DataSourceEswbTopic('omega_y', path=f'{topics_root}/nav/nav/omega/y', mult=57.32),
                        DataSourceEswbTopic('omega_z', path=f'{topics_root}/nav/nav/omega/z', mult=57.32)],
                        data_range=(-60, +60))

imu_a = ewChart([DataSourceEswbTopic('a_x', path=f'{topics_root}/nav/nav/a/x'),
                        DataSourceEswbTopic('a_y', path=f'{topics_root}/nav/nav/a/y'),
                        DataSourceEswbTopic('a_z', path=f'{topics_root}/nav/nav/a/z')],
                        data_range=(-15, +15))

mag = ewChart([DataSourceEswbTopic('mag_x', path=f'{topics_root}/nav/nav/mag/x', mult=1.0),
                        DataSourceEswbTopic('mag_y', path=f'{topics_root}/nav/nav/mag/y', mult=1.0),
                        DataSourceEswbTopic('mag_z', path=f'{topics_root}/nav/nav/mag/z', mult=1.0)],
                        data_range=(-30, +30))

hk_sine = ewChart([DataSourceEswbTopic('sine', path=f'{topics_root}/hk/sine'),
                        # DataSourceSinus('s1', iphase=0.0),
                        # DataSourceSinus('s2', iphase=1.0)
                   ],
                        data_range=(-1, +1))

manc_xy = ewCursor([(DataSourceEswbTopic('x', path=f'{topics_root}/cont/man_cont/direct/x'),
                          DataSourceEswbTopic('y', path=f'{topics_root}/cont/man_cont/direct/y'))])

mon.add_widget(ewGroup([imu_roll_pitch, ]))
mon.add_widget(ewGroup([manc_xy, imu_omega, imu_a, hk_sine]))
mon.add_widget(ewGroup([mag]))

mon.add_widget(mon.get_stat_widget())
mon.run()
