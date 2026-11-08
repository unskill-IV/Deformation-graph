from matplotlib import pyplot as plt
from openpyxl import load_workbook

def load_data(data_name):
    wb = load_workbook(f'data/{data_name}_g.xlsx', data_only=True, read_only=True)
    sheet_name = data_name[2:].split('_')[0]
    ws = load_workbook('data/2026_1103 Толщины, напряжения, деформации (В4,В5,П006,П007).xlsx',
                       data_only=True, read_only=True)[sheet_name]

    return wb, ws


def get_steps_count(book):


    return steps

def get_data(sheet):
    h = []
    d = []



    return h, d


file = input('Enter measurement name: ')

db, ds = load_data(file)
height, deformation = get_data(ds)
