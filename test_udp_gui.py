#!/usr/bin/env python3

import sys
from time import sleep
import ctypes
from typing import List

sys.path.append('./catpilot/c-atom/eswb/pytools')

from monitor import *
from eswbmon import *
from ds.datasources import *

from eswb import *

mon_bus_name = 'monitor'
telemetry_dir_name = 'telemetry'

args_parser = ArgParser()
args = args_parser.args

mon = EswbMonitor(monitor_bus_name=mon_bus_name, argv=sys.argv, tabs=True, )

imu_tab = mon.add_tab('IMU')
pres_tab = mon.add_tab('Pressure')
hk_tab = mon.add_tab('Houskeeping')
sdtl_tab = mon.add_tab('SDTL')

mon.mkdir(telemetry_dir_name)

basic_topics_root = mon_bus_name + '/' + telemetry_dir_name
drone_topics_root = basic_topics_root + '/' + 'drone'

cmd_sdtl_channel = SDTLchannel(name='cmd', ch_id=4, ch_type=SDTLchannelType.unrel)
mon.bridge_sdtl_udp(ip_in='0.0.0.0', port_in='20001', 
                    ip_out='192.168.1.27', port_out='20000', 
                    bridge_to='telemetry', 
                    additional_channels=[cmd_sdtl_channel])

# IMU
a = EwChart([DataSourceEswbTopic('ax', path=f'{basic_topics_root}/nav/nav/a/x'),
             DataSourceEswbTopic('ay', path=f'{basic_topics_root}/nav/nav/a/y'),
             DataSourceEswbTopic('az', path=f'{basic_topics_root}/nav/nav/a/z')])
omega = EwChart([DataSourceEswbTopic('wx', path=f'{basic_topics_root}/nav/nav/omega/x', mult=57.32),
                 DataSourceEswbTopic('wy', path=f'{basic_topics_root}/nav/nav/omega/y', mult=57.32),
                 DataSourceEswbTopic('wz', path=f'{basic_topics_root}/nav/nav/omega/z', mult=57.32)])
roll_pitch = EwChart([DataSourceEswbTopic('roll', path=f'{basic_topics_root}/nav/nav/roll', mult=57.32),
                 DataSourceEswbTopic('pitch', path=f'{basic_topics_root}/nav/nav/pitch', mult=57.32)])
yaw = EwChart([DataSourceEswbTopic('yaw', path=f'{basic_topics_root}/nav/nav/yaw', mult=57.32)])
temp = EwChart([DataSourceEswbTopic('tax', path=f'{basic_topics_root}/hk/hk/ta/x'),
             DataSourceEswbTopic('tay', path=f'{basic_topics_root}/hk/hk/ta/y'),
             DataSourceEswbTopic('taz', path=f'{basic_topics_root}/hk/hk/ta/z'),
             DataSourceEswbTopic('twx', path=f'{basic_topics_root}/hk/hk/tw/x'),
             DataSourceEswbTopic('twy', path=f'{basic_topics_root}/hk/hk/tw/y'),
             DataSourceEswbTopic('twz', path=f'{basic_topics_root}/hk/hk/tw/z')])

# Pressure
p = EwChart([DataSourceEswbTopic('pstat', path=f'{basic_topics_root}/nav/nav/pstat'),
             DataSourceEswbTopic('pdyn', path=f'{basic_topics_root}/nav/nav/pdyn')])
p_diff = EwChart([DataSourceEswbTopic('pdiff', path=f'{basic_topics_root}/nav/nav/pdiff')])
p_temp = EwChart([DataSourceEswbTopic('tadc', path=f'{basic_topics_root}/hk/hk/tadc')])

# Housekeeping
sin = EwChart([DataSourceEswbTopic('sin1', path=f'{basic_topics_root}/hk/sin1'),
               DataSourceEswbTopic('sin2', path=f'{basic_topics_root}/hk/sin2')])


imu_tab.add_widget(a)
imu_tab.add_widget(omega)
imu_tab.add_widget(roll_pitch)
imu_tab.add_widget(yaw)
imu_tab.add_widget(temp)

pres_tab.add_widget(p)
pres_tab.add_widget(p_diff)
pres_tab.add_widget(p_temp)

hk_tab.add_widget(sin)

sdtl_tab.add_widget(EwGroup([mon.get_stat_widget()]))

mon.app_window.print_bus_tree()
mon.run()
