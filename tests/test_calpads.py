import unittest
import time
import datetime as dt
import configparser
import logging
import sys
import pandas as pd
from ducttape-calpads import calpads as cp
from ducttape.exceptions import (
    InvalidLoginCredentials,
    ReportNotFound,
    InvalidIMAPParameters,
)

logger = logging.getLogger()
logger.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

config = configparser.ConfigParser()
config.read('./config/config.ini')

class TestCalpadsDataSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config_section_name = 'Calpads'
        args = {
            'hostname': config[config_section_name]['hostname'],
            'username': config[config_section_name]['username'],
            'password': config[config_section_name]['password'],
            'wait_time': int(config[config_section_name]['wait_time']),
            'temp_folder_path': config[config_section_name]['temp_folder_path']
        }
        cls.cp = cp.Calpads(**args)

    def setUp(self):
        self.assertTrue(isinstance(self.cp, cp.Calpads))

    def test_get_current_language_data(self):
        result = self.cp.get_current_language_data(1234567890)
        self.assertTrue(isinstance(result, pd.DataFrame))