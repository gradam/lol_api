import json
import os

from riotApi._utils import directory


class LocalData:
    def __init__(self, static_data):
        self.static_data = static_data

    def renew_all_info(self):
        self.renew_champions_info()
        self.renew_items_info()

    def renew_champions_info(self):
        data = self.static_data.champions_all(champData='all')
        self._save_to_json('champions.json', data)

    def renew_items_info(self):
        data = self.static_data.items_all(itemListData='all')
        self._save_to_json('items.json', data)

    def _ensure_folder_exist(self, path):
        try:
            os.mkdir(path)
        except FileExistsError:
            pass

    def _save_to_json(self, filename, data):
        path = os.path.join(directory, 'data')
        self._ensure_folder_exist(path)
        json_file = os.path.join(path, filename)
        with open(json_file, 'w') as out_file:
            json.dump(data, out_file)
