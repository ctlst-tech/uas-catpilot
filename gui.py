#!/usr/bin/env python3

import sys

sys.path.append("./catpilot/c-atom/eswb/pytools")

# from controls import *
from monitor import *
from eswbmon import *

mon_bus_name = 'monitor'
telemetry_dir_name = 'telemetry'

args_parser = ArgParser()
args = args_parser.args

mon = EswbMonitor(monitor_bus_name=mon_bus_name, argv=sys.argv, tabs=True)

front_tab = mon.add_tab('Main')
nav_data_tab = mon.add_tab('Nav Data')
imu_tab = mon.add_tab('IMU')
control_tab = mon.add_tab('Control')
rel_map_tab = mon.add_tab('Rel Map')
map_tab = mon.add_tab('Map')
raw_data_tab = mon.add_tab('Raw data')
sdtl_tab = mon.add_tab('SDTL')

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

ds_yaw = DataSourceEswbTopic('yaw', path=f'{topics_root}/nav/nav/yaw', mult=57.32)

hi = EwHeadingIndicator([ds_yaw])

ds_mag_azimuth = DataSourceEswbTopic('azimuth', path=f'{topics_root}/nav/nav/azimuth', mult=57.32)

compass = EwHeadingIndicator([ds_mag_azimuth])

imu_roll_pitch = EwChart([DataSourceEswbTopic('roll', path=f'{topics_root}/nav/nav/roll', mult=57.32),
                        DataSourceEswbTopic('pitch', path=f'{topics_root}/nav/nav/pitch', mult=57.32)],
                        data_range=(-60, +60))

imu_omega = EwChart([DataSourceEswbTopic('omega_x', path=f'{topics_root}/nav/nav/omega/x', mult=57.32),
                        DataSourceEswbTopic('omega_y', path=f'{topics_root}/nav/nav/omega/y', mult=57.32),
                        DataSourceEswbTopic('omega_z', path=f'{topics_root}/nav/nav/omega/z', mult=57.32)],
                        data_range=(-60, +60))

ds_accel_x = DataSourceEswbTopic('a_x', path=f'{topics_root}/nav/nav/a/x')
ds_accel_y = DataSourceEswbTopic('a_y', path=f'{topics_root}/nav/nav/a/y')
ds_accel_z = DataSourceEswbTopic('a_z', path=f'{topics_root}/nav/nav/a/z')

imu_a = EwChart([ds_accel_x,
                 ds_accel_y,
                 ds_accel_z,],
                        data_range=(-15, +15))

norm_ind_magnitude_ds = DataSourceEswbTopic('mag', path=f'{topics_root}/nav/nav/ind_magnitude')

ds_magn_x = DataSourceEswbTopic('mag_x', path=f'{topics_root}/nav/nav/induction/x')
ds_magn_y = DataSourceEswbTopic('mag_y', path=f'{topics_root}/nav/nav/induction/y')
ds_magn_z = DataSourceEswbTopic('mag_z', path=f'{topics_root}/nav/nav/induction/z')

mag = EwChart([ds_magn_x,
               ds_magn_y,
               ds_magn_z,
               norm_ind_magnitude_ds],
                data_range=(-0.7, +0.7))

hk_sine = EwChart([DataSourceEswbTopic('sine', path=f'{topics_root}/hk/sine'),
                        # DataSourceSinus('s1', iphase=0.0),
                        # DataSourceSinus('s2', iphase=1.0)
                   ],
                   data_range=(-1, +1))

hk_Vbat = EwChart([DataSourceEswbTopic('Vbat', path=f'{topics_root}/hk/Vbat'),
                   DataSourceEswbTopic('Vbat_min', path=f'{topics_root}/hk/Vbat_min'),
                   DataSourceEswbTopic('Vbat_max', path=f'{topics_root}/hk/Vbat_max')
                   ])

hk_CurrBat = EwChart([DataSourceEswbTopic('Curr', path=f'{topics_root}/hk/Curr'),
                   DataSourceEswbTopic('Curr_min', path=f'{topics_root}/hk/Curr_min'),
                   DataSourceEswbTopic('Curr_max', path=f'{topics_root}/hk/Curr_max')
                   ])

manc_xy = EwCursor([
    (DataSourceEswbTopic('x', path=f'{topics_root}/cont/cont/direct/x'),
                          DataSourceEswbTopic('y', path=f'{topics_root}/cont/cont/direct/y')),
    (DataSourceEswbTopic('x', path=f'{topics_root}/cont/cont/sol/x'),
                          DataSourceEswbTopic('y', path=f'{topics_root}/cont/cont/sol/y'))
])

ds_gnss_lat = DataSourceEswbTopic(name='gnss_lat', path=f'{topics_root}/nav/nav/gnss_pos/x')
ds_gnss_lon = DataSourceEswbTopic(name='gnss_lon', path=f'{topics_root}/nav/nav/gnss_pos/y')
ds_gnss_alt = DataSourceEswbTopic(name='gnss_alt', path=f'{topics_root}/nav/nav/gnss_pos/z')

ds_lat = DataSourceEswbTopic(name='lat', path=f'{topics_root}/nav/nav/pos/x')
ds_lon = DataSourceEswbTopic(name='lon', path=f'{topics_root}/nav/nav/pos/y')
ds_alt = DataSourceEswbTopic(name='alt', path=f'{topics_root}/nav/nav/pos/z')

ds_gnss_vel_n = DataSourceEswbTopic(name='gnss_vel_n', path=f'{topics_root}/nav/nav/gnss_vel/x')
ds_gnss_vel_e = DataSourceEswbTopic(name='gnss_vel_e', path=f'{topics_root}/nav/nav/gnss_vel/y')
ds_gnss_vel_d = DataSourceEswbTopic(name='gnss_vel_d', path=f'{topics_root}/nav/nav/gnss_vel/z')
ds_vel_n = DataSourceEswbTopic(name='vel_n', path=f'{topics_root}/nav/nav/vel/x')
ds_vel_e = DataSourceEswbTopic(name='vel_e', path=f'{topics_root}/nav/nav/vel/y')
ds_vel_d = DataSourceEswbTopic(name='vel_d', path=f'{topics_root}/nav/nav/vel/z')

vel_body_longit = DataSourceEswbTopic(name='vel_body_longit', path=f'{topics_root}/cont/cont/vel_body/x')
vel_body_transv = DataSourceEswbTopic(name='vel_body_transv', path=f'{topics_root}/cont/cont/vel_body/y')
vel_body_vert = DataSourceEswbTopic(name='vel_body_vert', path=f'{topics_root}/cont/cont/vel_body/z')

desired_vel_body_longit = DataSourceEswbTopic(name='desired_vel_body_longit', path=f'{topics_root}/cont/cont/desired_vel_body/x')
desired_vel_body_transv = DataSourceEswbTopic(name='desired_vel_body_transv', path=f'{topics_root}/cont/cont/desired_vel_body/y')
desired_vel_body_vert = DataSourceEswbTopic(name='desired_vel_body_vert', path=f'{topics_root}/cont/cont/desired_vel_body/z')

modes = EwTable(caption='Modes', data_sources=[
    DataSourceEswbTopic(name='armed', path=f'{topics_root}/cont/cont_mode/armed'),
    DataSourceEswbTopic(name='enable_angrate', path=f'{topics_root}/cont/cont_mode/enable_angrate'),
    DataSourceEswbTopic(name='enable_angpos', path=f'{topics_root}/cont/cont_mode/enable_angpos'),
    DataSourceEswbTopic(name='enable_vel', path=f'{topics_root}/cont/cont_mode/enable_vel'),
    DataSourceEswbTopic(name='enable_auto', path=f'{topics_root}/cont/cont_mode/enable_auto'),
    DataSourceEswbTopic(name='hold_yaw_cmd', path=f'{topics_root}/cont/cont_mode/hold_yaw_cmd'),
    DataSourceEswbTopic(name='vel_enabled', path=f'{topics_root}/cont/cont_mode/vel_enabled'),
    DataSourceEswbTopic(name='gnss_prec', path=f'{topics_root}/nav/nav/gnss_prec'),
    DataSourceEswbTopic(name='gnss_ready', path=f'{topics_root}/nav/nav/gnss_ready'),
])

nav_data_table = EwTable(caption='Nav Data', data_sources=[
    ds_gnss_lat,
    ds_gnss_lon,
    ds_gnss_alt,
    ds_gnss_vel_n,
    ds_gnss_vel_e,
    ds_gnss_vel_d,
    ds_lat,
    ds_lon,
    ds_alt,
    ds_vel_n,
    ds_vel_e,
    ds_vel_d,
    ds_accel_x,
    ds_accel_y,
    ds_accel_z,
    ds_magn_x,
    ds_magn_y,
    ds_magn_z,
])

gnss_prec = EwChart([DataSourceEswbTopic('gnss_prec', path=f'{topics_root}/nav/nav/gnss_prec')])

map = EwLocationMap(
    [('gnss', ds_gnss_lat, ds_gnss_lon, ds_mag_azimuth), ('est', ds_lat, ds_lon, ds_yaw)],
    with_control=True)

rel_map = EwRelativePosition([
    DataSourceSinus('plane_phi', mult=360),
    DataSourceConst('plane_r', value=60),
    DataSourceSinus('plane_course', iphase=0.0, mult=360),

    DataSourceSinus('base_phi', iphase=0.5, mult=360),
    DataSourceConst('base_r', value=120),
])

ind_magn_chart = EwChart([norm_ind_magnitude_ds])

pos_n_chart = EwChart([ds_gnss_lat, ds_lat])
pos_e_chart = EwChart([ds_gnss_lon, ds_lon])
pos_v_chart = EwChart([ds_gnss_alt, ds_alt])

vel_n_chart = EwChart([ds_gnss_vel_n, ds_vel_n])
vel_e_chart = EwChart([ds_gnss_vel_e, ds_vel_e])
vel_v_chart = EwChart([ds_gnss_vel_d, ds_vel_d])

vel_body_chart_longit = EwChart([vel_body_longit, desired_vel_body_longit])
vel_body_chart_transv = EwChart([vel_body_transv, desired_vel_body_transv])
vel_body_chart_vert = EwChart([vel_body_vert, desired_vel_body_vert])

front_tab.add_widget(EwGroup([ai, hi, compass, manc_xy, modes, mon.get_small_widget()]))
front_tab.add_widget(EwGroup([imu_roll_pitch, gnss_prec, hk_sine]))
front_tab.add_widget(EwGroup([hk_Vbat, hk_CurrBat]))
# front_tab.add_widget(EwGroup([]))

nav_data_tab.add_widget(nav_data_table)

imu_tab.add_widget(EwGroup([pos_n_chart, pos_e_chart, pos_v_chart]))
imu_tab.add_widget(EwGroup([vel_n_chart, vel_e_chart, vel_v_chart]))

imu_tab.add_widget(ind_magn_chart)

control_tab.add_widget(vel_body_chart_longit)
control_tab.add_widget(vel_body_chart_transv)
control_tab.add_widget(vel_body_chart_vert)

map_tab.add_widget(map)

rel_map_tab.add_widget(rel_map)

raw_data_tab.add_widget(imu_omega)
raw_data_tab.add_widget(imu_a)
raw_data_tab.add_widget(mag)

sdtl_tab.add_widget(EwGroup([mon.get_stat_widget()]))
mon.run()
