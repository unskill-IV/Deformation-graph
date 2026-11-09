import sys
sys.path.append("../Deformation-data/")
from graph_module import *

file = input('Enter measurement name: ')

ds_1, ds_2 = load_data(file)
height, deformation = get_data(ds_2)
