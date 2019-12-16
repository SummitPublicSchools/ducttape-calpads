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

EXTRACTS = ['ssid', 'crsc', 'crse', 'sass', 'stas', 'scte',
            'scsc', 'scse', 'sdis', 'sdem', 'sprg', 'cenr',
            'sped', 'sela', 'sinf', 'ssrv', 'directcertification']
YEAR_ONLY_EXTRACTS = ['crsc', 'crse', 'sass', 'scsc', 'stas',
                    'scte', 'scse', 'sdis']

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
        self.cp.driver.quit()

    def test_request_extracts_nonyear(self):
        for extract in EXTRACTS:
            if extract not in YEAR_ONLY_EXTRACTS and extract != 'cenr':
                with self.subTest(extract=extract):
                    self.assertTrue(self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                                            extract_name=extract))
    
    def test_request_extracts_academic_year(self):
        for extract in EXTRACTS:
            if extract in YEAR_ONLY_EXTRACTS or extract == 'cenr':
                with self.subTest(extract=extract):
                    self.assertTrue(self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                                            extract_name=extract,
                                                            academic_year=config['Calpads']['current_academic_year']))

    def test_request_extracts_by_date_range(self):
        test_extracts = list(set(EXTRACTS) - set(YEAR_ONLY_EXTRACTS))
        for extract in test_extracts:
            with self.subTest(extract=extract):
                self.assertTrue(self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                                        extract_name=extract,
                                                        by_date_range=True,
                                                        start_date='08/01/2019',
                                                        end_date='07/01/2020'))
    
    def test_download_extracts_dataframe(self):
        for extract in EXTRACTS:
            with self.subTest(extract=extract):
                self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                        extract_name=extract,
                                        academic_year=config['Calpads']['current_academic_year'])
                self.assertIsInstance(self.cp.download_extract(lea_code=config['Calpads']['test_lea'],
                                                                extract_name=extract), 
                                        pd.DataFrame)
    
    def test_download_extract_ssid_download(self):
        for extract in EXTRACTS:
            with self.subTest(extract=extract):
                self.cp.request_extract(lea_code=config['Calpads']['test_lea'],
                                        extract_name=extract,
                                        academic_year=config['Calpads']['current_academic_year'])
                self.cp.download_extract(lea_code=config['Calpads']['test_lea'], 
                                        extract_name=extract,
                                        temp_folder_name=config['Calpads']['temp_folder_path'])
                self.assertTrue(len(os.listdir(config['Calpads']['temp_folder_path'])) == 1)
