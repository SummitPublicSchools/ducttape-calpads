import unittest
import time
import datetime as dt
import configparser
import logging
import sys
import os
import shutil
import pandas as pd
from ducttape_calpads import calpads as cp
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

    def test_download_url_report(self):
        with self.assertRaises(NotImplementedError):
            self.cp.download_url_report('testing.com', '.')

    def test_get_current_language_data(self):
        result = self.cp.get_current_language_data(1234567890)
        self.assertTrue(isinstance(result, pd.DataFrame))


class TestCalpadsExtracts(unittest.TestCase):
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
    
    def tearDown(self):
        if os.path.exists(config['Calpads']['temp_folder_path']):
            shutil.rmtree(config['Calpads']['temp_folder_path'])

    def test_request_ssid(self):
        self.assertTrue(self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                                extract_name='ssid'))

    def test_request_ssid_by_date_range(self):
        self.assertTrue(self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                                extract_name='ssid',
                                                by_date_range=True,
                                                start_date='08/01/2019',
                                                end_date='07/01/2020'))
    
    def test_download_extract_ssid_df(self):
        self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                                extract_name='ssid')
        self.assertIsInstance(self.cp.download_extract(lea_code=config['Calpads']['test_lea'],
                                                        extract_name='ssid'), pd.DataFrame)
    
    def test_download_extract_ssid_download(self):
        self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                                extract_name='ssid')
        self.cp.download_extract(config['Calpads']['test_lea'], 'ssid',
                                temp_folder_name=config['Calpads']['temp_folder_path'])
        self.assertTrue(len(os.listdir(config['Calpads']['temp_folder_path'])) == 1)
