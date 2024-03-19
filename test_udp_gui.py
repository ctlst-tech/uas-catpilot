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

main_tab = mon.add_tab('Main')
hk_tab = mon.add_tab('Houskeeping')
sdtl_tab = mon.add_tab('SDTL')

mon.mkdir(telemetry_dir_name)

basic_topics_root = mon_bus_name + '/' + telemetry_dir_name
drone_topics_root = basic_topics_root + '/' + 'drone'

cmd_sdtl_channel = SDTLchannel(name='cmd', ch_id=4, ch_type=SDTLchannelType.unrel)
mon.bridge_sdtl_udp(ip_in='0.0.0.0', port_in='20001',
                    ip_out='192.168.1.21', port_out='20000',
                    bridge_to='telemetry',
                    additional_channels=[cmd_sdtl_channel])

ax = DataSourceEswbTopic('ax', path=f'{basic_topics_root}/nav/ang/a/x')
ay = DataSourceEswbTopic('ay', path=f'{basic_topics_root}/nav/ang/a/y')
az = DataSourceEswbTopic('az', path=f'{basic_topics_root}/nav/ang/a/z')
wx = DataSourceEswbTopic('wx', path=f'{basic_topics_root}/nav/ang/omega/x', mult=57.32)
wy = DataSourceEswbTopic('wy', path=f'{basic_topics_root}/nav/ang/omega/y', mult=57.32)
wz = DataSourceEswbTopic('wz', path=f'{basic_topics_root}/nav/ang/omega/z', mult=57.32)
roll = DataSourceEswbTopic('roll', path=f'{basic_topics_root}/nav/ang/roll', mult=57.32)
pitch = DataSourceEswbTopic('pitch', path=f'{basic_topics_root}/nav/ang/pitch', mult=57.32)
yaw = DataSourceEswbTopic('yaw', path=f'{basic_topics_root}/nav/ang/yaw', mult=57.32)

pstat = DataSourceEswbTopic('pstat', path=f'{basic_topics_root}/nav/pres/pstat')
pdyn = DataSourceEswbTopic('pdyn', path=f'{basic_topics_root}/nav/pres/pdyn')
pdiff = DataSourceEswbTopic('pdiff', path=f'{basic_topics_root}/nav/pres/pdiff')

altitude_bar = DataSourceEswbTopic('altitude_bar', path=f'{basic_topics_root}/nav/air/altitude_bar')
airspeed = DataSourceEswbTopic('airspeed', path=f'{basic_topics_root}/nav/air/airspeed')

tax = DataSourceEswbTopic('tax', path=f'{basic_topics_root}/dev/imu/t/ta/x')
tay = DataSourceEswbTopic('tay', path=f'{basic_topics_root}/dev/imu/t/ta/y')
taz = DataSourceEswbTopic('taz', path=f'{basic_topics_root}/dev/imu/t/ta/z')
twx = DataSourceEswbTopic('twx', path=f'{basic_topics_root}/dev/imu/t/tw/x')
twy = DataSourceEswbTopic('twy', path=f'{basic_topics_root}/dev/imu/t/tw/y')
twz = DataSourceEswbTopic('twz', path=f'{basic_topics_root}/dev/imu/t/tw/z')
tadc = DataSourceEswbTopic('tadc', path=f'{basic_topics_root}/dev/imu/t/tadc')

io_adc1_ch0 = DataSourceEswbTopic('io_adc1_ch0', path=f'{basic_topics_root}/dev/adc/voltage/ch0')
io_adc1_ch1 = DataSourceEswbTopic('io_adc1_ch1', path=f'{basic_topics_root}/dev/adc/voltage/ch1')
io_adc1_ch2 = DataSourceEswbTopic('io_adc1_ch2', path=f'{basic_topics_root}/dev/adc/voltage/ch2')
io_adc1_ch3 = DataSourceEswbTopic('io_adc1_ch3', path=f'{basic_topics_root}/dev/adc/voltage/ch3')
io_adc1_ch4 = DataSourceEswbTopic('io_adc1_ch4', path=f'{basic_topics_root}/dev/adc/voltage/ch4')
io_adc1_ch5 = DataSourceEswbTopic('io_adc1_ch5', path=f'{basic_topics_root}/dev/adc/voltage/ch5')
io_adc1_ch6 = DataSourceEswbTopic('io_adc1_ch6', path=f'{basic_topics_root}/dev/adc/voltage/ch6')
io_adc1_ch7 = DataSourceEswbTopic('io_adc1_ch7', path=f'{basic_topics_root}/dev/adc/voltage/ch7')
io_adc2_ch0 = DataSourceEswbTopic('io_adc2_ch0', path=f'{basic_topics_root}/dev/adc/voltage/ch8')
io_adc2_ch1 = DataSourceEswbTopic('io_adc2_ch1', path=f'{basic_topics_root}/dev/adc/voltage/ch9')
io_adc2_ch2 = DataSourceEswbTopic('io_adc2_ch2', path=f'{basic_topics_root}/dev/adc/voltage/ch10')
io_adc2_ch3 = DataSourceEswbTopic('io_adc2_ch3', path=f'{basic_topics_root}/dev/adc/voltage/ch11')
io_adc2_ch4 = DataSourceEswbTopic('io_adc2_ch4', path=f'{basic_topics_root}/dev/adc/voltage/ch12')
io_adc2_ch5 = DataSourceEswbTopic('io_adc2_ch5', path=f'{basic_topics_root}/dev/adc/voltage/ch13')
io_adc2_ch6 = DataSourceEswbTopic('io_adc2_ch6', path=f'{basic_topics_root}/dev/adc/voltage/ch14')
io_adc2_ch7 = DataSourceEswbTopic('io_adc2_ch7', path=f'{basic_topics_root}/dev/adc/voltage/ch15')

sin = EwChart([DataSourceEswbTopic('sin1', path=f'{basic_topics_root}/hk/sin1'),
               DataSourceEswbTopic('sin2', path=f'{basic_topics_root}/hk/sin2')])

accel = EwChart([ax, ay, az], title="Accelerations",
                labels={'left': 'm/s²', 'bottom': 'time, s'})
gyro = EwChart([wx, wy, wz], title="Angular rates",
               labels={'left': '1/s', 'bottom': 'time, s'})
roll_pitch = EwChart([roll, pitch], title="Angles",
                     labels={'left': 'grad', 'bottom': 'time, s'})
yaw = EwChart([yaw], title="Angles")
accel_gyro_temp = EwChart([tax, tay, taz, twx, twy, twz], title="Sensor temperatures",
                          labels={'left': '°C', 'bottom': 'time, s'})

pstat_pdyn = EwChart([pstat, pdyn], title="Static and dynamic pressure")
pdiff = EwChart([pdiff], title="Differential pressure")
adc_temp = EwChart([tadc], title="ADC temperature")

altitude_bar = EwChart([altitude_bar], title="Barometric altitude")
airspeed = EwChart([airspeed], title="Airspeed")

# io_adc1 = EwChart([io_adc1_ch0, io_adc1_ch1, io_adc1_ch2, io_adc1_ch3, io_adc1_ch4, io_adc1_ch5], title="IO ADC 1 channels")
# io_adc2 = EwChart([io_adc2_ch0, io_adc2_ch1, io_adc2_ch2, io_adc2_ch3, io_adc2_ch4, io_adc2_ch5], title="IO ADC 2 channels")
io_adc1_ch0 = EwChart([io_adc1_ch0], title="IO ADC1 ch0")
io_adc1_ch1 = EwChart([io_adc1_ch1], title="IO ADC1 ch1")
io_adc1_ch2 = EwChart([io_adc1_ch2], title="IO ADC1 ch2")
io_adc1_ch3 = EwChart([io_adc1_ch3], title="IO ADC1 ch3")
io_adc1_ch4 = EwChart([io_adc1_ch4], title="IO ADC1 ch4")
io_adc1_ch5 = EwChart([io_adc1_ch5], title="IO ADC1 ch5")
io_adc1_ch6 = EwChart([io_adc1_ch6], title="IO ADC1 ch6")
io_adc1_ch7 = EwChart([io_adc1_ch7], title="IO ADC1 ch7")
io_adc2_ch0 = EwChart([io_adc2_ch0], title="IO ADC2 ch0")
io_adc2_ch1 = EwChart([io_adc2_ch1], title="IO ADC2 ch1")
io_adc2_ch2 = EwChart([io_adc2_ch2], title="IO ADC2 ch2")
io_adc2_ch3 = EwChart([io_adc2_ch3], title="IO ADC2 ch3")
io_adc2_ch4 = EwChart([io_adc2_ch4], title="IO ADC2 ch4")
io_adc2_ch5 = EwChart([io_adc2_ch5], title="IO ADC2 ch5")
io_adc2_ch6 = EwChart([io_adc2_ch6], title="IO ADC2 ch6")
io_adc2_ch7 = EwChart([io_adc2_ch7], title="IO ADC2 ch7")

main_tab.add_widget(EwGroup([accel, gyro, roll_pitch, accel_gyro_temp]))
main_tab.add_widget(EwGroup([pstat_pdyn, pdiff, adc_temp, altitude_bar, airspeed]))
main_tab.add_widget(EwGroup([io_adc1_ch0, io_adc1_ch1, io_adc1_ch2, io_adc1_ch3, io_adc1_ch4, io_adc1_ch5, io_adc1_ch6, io_adc1_ch7]))
main_tab.add_widget(EwGroup([io_adc2_ch0, io_adc2_ch1, io_adc2_ch2, io_adc2_ch3, io_adc2_ch4, io_adc2_ch5, io_adc2_ch6, io_adc2_ch7]))

hk_tab.add_widget(sin)

sdtl_tab.add_widget(EwGroup([mon.get_stat_widget()]))

mon.app_window.print_bus_tree()
mon.run()
