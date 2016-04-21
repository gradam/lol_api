import os
import json

from riotApi import directory
from riotApi.lol_static_data import all_champions_info, all_items_info


def renew_all_info():
    renew_champions_info()
    renew_items_info()


def renew_champions_info():
    data = all_champions_info(champData='all')
    _save_to_json('champions.json', data)


def renew_items_info():
    data = all_items_info(itemListData='all')
    _save_to_json('items.json', data)


def _ensure_folder_exist(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def _save_to_json(filename, data):
    path = os.path.join(directory, 'data')
    _ensure_folder_exist(path)
    json_file = os.path.join(path, filename)
    with open(json_file, 'w') as out_file:
        json.dump(data, out_file)
