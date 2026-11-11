from modules.graph_module import *

basic_style = [
    'o-m',
    'o-b',
    'o--c'
]
temp_list = [
    '3-В4_deformation_2018_6MHz_sensor_3',
    '3-В5_stresses_2018_6MHz_sensor_3',
    '3-П06_deformation_2018_6MHz_sensor_3',
    '3-П07_stresses_2018_6MHz_sensor_3'
]
temp_metrics = [
    'time',
    'velocity',
    'Poisson',
    'Anisotropy'
]
title_dict = {
    'time' : 'Зависимость времени от деформации',
    'velocity' : 'Зависимость скорости от деформации',
    'Poisson' : 'Зависимость коэффициента поперечной деформации от деформации',
    'Anisotropy' : 'Зависимость акустической анизотропии от деформации'
}
y_label_dict = {
    'time' : 'Время, мс',
    'velocity' : 'Скорость, м/с',
    'Poisson' : 'Коэффициент поперечной деформации',
    'Anisotropy' : 'Акустическая анизотропия'
}
major_step_dict = {
    'time' : 0.05,
    'velocity' : 0.01,
    'Poisson' : 0.001,
    'Anisotropy' : 0.002
}
def_x_label = 'Истинная деформация, %'

for iter in temp_list:
    for metr in temp_metrics:
        plot_metric(
            iter,
            metr,
            basic_style,
            title_dict[metr],
            def_x_label,
            y_label_dict[metr],
            major_step_dict[metr],
            True,
            False
        )
