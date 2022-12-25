from tkinter import Tk
from numpy import isnan, set_printoptions, seterr
from typing import Optional
from pandas import read_excel
from pyexcel import load_book
from tkinter.filedialog import askopenfilename
from pandas import set_option
from sys import exit, maxsize

set_option('display.max_rows', None)
set_option('display.max_columns', None)
set_printoptions(threshold=maxsize, precision=2, linewidth=100000)
seterr(invalid='ignore')

DEFAULT = {
    "folder": "exel",
    "file": "hyperbolic-2003-2020-final-1401.xlsx",
    "sheet_name": "SampleFile"
}


def indexing(labels: list, msg: str, sep: Optional[str] = ': '):
    for index, label in enumerate(labels):
        print(index, label, sep=sep)
    try:
        labels_number = input(f'{msg} [q for exit]: ')
        if labels_number == 'q':
            exit()
        return labels[int(labels_number)]
    except Exception as e:
        print(e.__repr__())
        exit()


def get_file_name(*, exel_name=None, sheet_name=None):
    if exel_name is None:
        Tk().withdraw()
        exel_name = askopenfilename()
    if sheet_name is None:
        sheet_name = indexing(
            labels=load_book(file_name=exel_name).sheet_names(),
            msg="Pick Exel sheet You Want To Load")
    return exel_name, sheet_name


def exel_reader(*, exel_name=None, sheet_name=None):
    try:
        exel_name, sheet_name = get_file_name(exel_name=exel_name, sheet_name=sheet_name)
        data_sheet = read_excel(io=exel_name, sheet_name=sheet_name, header=0).to_numpy()
        return data_sheet
    except Exception as error:
        print(error.__repr__())
        exit()


def separator(data_sheet) -> dict:
    result = {}
    tmp = {
        "name": [],
        "Days": [],
        "SnowFall": []}
    counter = 1
    for record in data_sheet:
        if isnan(record[1]) or isnan(record[2]):
            if tmp["name"]:
                result[f'{counter}'] = {
                    "name": f'{tmp["name"][0]}:{tmp["name"][-1]}',
                    "Days": tmp["Days"],
                    "SnowFall": tmp["SnowFall"]}
                counter += 1
                tmp = {
                    "name": [],
                    "Days": [],
                    "SnowFall": []}
        else:
            tmp["name"].append(record[0])
            tmp["Days"].append(record[1])
            tmp["SnowFall"].append(record[2])

    result[f'{counter}'] = {
        "name": f'{tmp["name"][0]}:{tmp["name"][-1]}',
        "Days": tmp["Days"],
        "SnowFall": tmp["SnowFall"]}
    return result
