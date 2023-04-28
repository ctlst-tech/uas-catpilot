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

front_tab = mon.add_tab('Test')
sdtl_tab = mon.add_tab('SDTL')

mon.mkdir(telemetry_dir_name)

basic_topics_root = mon_bus_name + '/' + telemetry_dir_name
drone_topics_root = basic_topics_root + '/' + 'drone'

cmd_sdtl_channel = SDTLchannel(name='cmd', ch_id=4, ch_type=SDTLchannelType.unrel)
mon.bridge_sdtl_udp(ip_in='0.0.0.0', port_in='20001', 
                    ip_out='192.168.1.27', port_out='20000', 
                    bridge_to='telemetry', 
                    additional_channels=[cmd_sdtl_channel])

hk_sin1 = EwChart([DataSourceEswbTopic('sin1', path=f'{basic_topics_root}/hk/sin1'),], data_range=(-1, +1))
hk_sin2 = EwChart([DataSourceEswbTopic('sin2', path=f'{basic_topics_root}/hk/sin2'),], data_range=(-1, +1))

front_tab.add_widget(hk_sin1)
front_tab.add_widget(hk_sin2)
sdtl_tab.add_widget(EwGroup([mon.get_stat_widget()]))

mon.app_window.print_bus_tree()
mon.run()
