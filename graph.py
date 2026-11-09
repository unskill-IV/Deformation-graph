import sys
sys.path.append("../Deformation-data/")
from graph_module import *

file = input('Enter measurement name: ')

ds_1, ds_2 = load_data(file)
steps = get_steps_count(ds_1)
deformation = get_deformation(ds_2, steps)

