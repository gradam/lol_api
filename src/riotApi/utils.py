# encoding: utf-8


def get_api_key():
    with open('api_key.txt', 'r') as key_file:
        key = key_file.readline()
    return key
