# encoding: utf-8
import json
import os


def get(value):
    try:
        if isinstance(value, int):
            return ID_to_name[value]
        else:
            return name_to_id[value]
    except KeyError:
        raise ValueError


class ChampionsID:
    def __init__(self):
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
        champions_id_data_file = os.path.join(data_dir, 'championsID.json')
        self.id_to_name = self.load_json(champions_id_data_file)

    @staticmethod
    def load_json():
        pass
