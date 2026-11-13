from modules.graph_module import plot_metric

basic_style = [
    'o--m',
    'o--b',
    'o-.c'
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
    'Anisotropy',
    'Poisson'
]
title_dict = {
    'time' : 'Зависимость времени от деформации',
    'velocity' : 'Зависимость скорости от деформации',
    'Poisson' : 'Зависимость коэффициента поперечной деформации от деформации',
    'Anisotropy' : 'Зависимость акустической анизотропии от деформации'
}
y_label_dict = {
    'time' : 'Время, мкс',
    'velocity' : 'Скорость, км/с',
    'Poisson' : 'Коэффициент поперечной деформации',
    'Anisotropy' : 'Акустическая анизотропия'
}
major_step_dict = {
    'time' : 0.05,
    'velocity' : 0.01,
    'Poisson' : 0.001,
    'Anisotropy' : 0.002
}
fig_size_dict = {
    'width' : 16,
    'height' : 16,
    'dpi' : 100
}
def_x_step = 1.0
def_x_label = 'Истинная деформация, %'
def_tick_fontsize = 26

for iter in temp_list[2:]:
    for metr in temp_metrics[:-1]:
        plot_metric(
            data_name=iter,
            metric=metr,
            style=basic_style,
            title=title_dict[metr],
            x_label=def_x_label,
            y_label=y_label_dict[metr],
            figwidth=fig_size_dict['width'],
            figheight=fig_size_dict['height'],
            figdpi=fig_size_dict['dpi'],
            major_x_step=def_x_step,
            major_y_step=major_step_dict[metr],
            major_tick_fontsize=def_tick_fontsize,
            do_t3=False,
            do_save=True,
            do_show=False
        )
        print(f'Metric {metr!r} from {iter!r} is plotted.')
