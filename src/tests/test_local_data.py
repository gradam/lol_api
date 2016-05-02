# encoding: utf-8
from unittest.mock import mock_open

import pytest

from tests.utils import test_api_key, mock_request_get
from riotApi import Client


local_data = Client(test_api_key, unlimited=True).LocalData


def raise_file_exists_error(path):
    raise FileExistsError


@pytest.fixture(autouse=True)
def mock_open_func(mocker):
    m = mock_open()
    mocker.patch('builtins.open', m, create=True)


@pytest.fixture(autouse=True)
def mock_mkdir(mocker):
    mocker.patch('os.mkdir', lambda path: None, create=True)


def test_renew_champions_info():
    local_data.renew_champions_info()


def test_renew_items_info():
    local_data.renew_items_info()


def test_ensure_folder_exist():
    local_data._ensure_folder_exist('path')


def test_ensure_folder_exist_no_error(mocker):
    mocker.patch('os.mkdir', raise_file_exists_error, create=True)
    local_data._ensure_folder_exist('path')


def test_save_to_json():
    local_data._save_to_json('file', 'data')


def test_renew_all_info():
    local_data.renew_all_info()
