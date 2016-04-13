# encoding: utf-8
import os


def get_api_key():
    file_path = os.path.join(os.path.dirname(__file__), 'api_key.txt')
    with open(file_path, 'r') as key_file:
        key = key_file.readline()
    return key
