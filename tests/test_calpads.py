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
ODS_REPORTS = ['1.1', '1.2', '1.3', '1.5', '1.9', '1.10', '1.17', '1.18', 
                '1.19', '1.20', '2.2', '2.8', '5.6', '5.7', '5.8', '5.9',
                 '8.1', '8.1a', '8.1b', '8.2', '9.1', '9.2', '10.1', '11.1',
                 '12.1', '2.4', '2.5', '2.6', '2.7', '2.11', '3.1', '3.2', 
                 '3.3', '3.6', '3.7', '3.8', '4.1', '4.3', '4.4', '3.9', 
                 '3.10', '3.11', '3.12', '3.13', '3.14', '3.15', '5.1', 
                 '5.2', '5.3', '5.4', '5.5']
SNAPSHOT_REPORTS = ['1.0', '1.0a', '1.1', '1.2', '1.3', '1.4', '1.5',
                    '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12', 
                    '1.13', '1.14', '1.17', '1.18', '2.1', '2.2', '2.8',
                    '2.9', '2.10', '2.12', '2.13', '8.1', '8.1a', '8.1b',
                    '8.1c', '16.1', '16.2', '16.3', '16.5', '16.6', '2.4',
                    '2.5', '2.6', '2.7', '2.11', '2.14', '3.1', '3.2', '3.3',
                    '3.6', '3.7', '3.8', '4.1', '4.2', '4.3', '4.4', '4.5',
                    '17.1', '17.2', '3.9', '3.10', '3.11', '3.14', '3.15',
                    '3.16', '3.17', '3.18', '5.1', '5.2', '5.3', '1.21',
                    '1.21', '5.4', '5.5', '8.1eoy3', '14.1', '14.2']

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

    def tearDown(self):
        if os.path.exists(config['Calpads']['temp_folder_path']):
            shutil.rmtree(config['Calpads']['temp_folder_path'])
        try:
            if self.cp.driver.service.is_connectable():
                self.cp.driver.quit()
        except AttributeError:
            pass

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
        if self.cp.driver.service.is_connectable():
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

class TestCalpadsReports(unittest.TestCase):
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
        if self.cp.driver.service.is_connectable():
            self.cp.driver.quit()
    
    def test_download_snapshot_report(self):
        for snapshot in SNAPSHOT_REPORTS:
            with self.subTest(snapshot=snapshot):
                try:
                    self.assertTrue(isinstance(self.cp.download_snapshot_report(lea_code=config['Calpads']['test_lea'],
                                                                        report_code=snapshot, 
                                                                        dry_run=False), 
                                            pd.DataFrame))
                except:
                    #Need to make sure the driver still closes even if it fails for some reason -- wasn't always happening
                    if self.cp.driver.service.is_connectable():
                        self.cp.driver.quit()
                    raise
    
    def test_download_ods_report(self):
        for ods in ODS_REPORTS:
            with self.subTest(ods=ods):
                try:
                    self.assertTrue(isinstance(self.cp.download_ods_report(lea_code=config['Calpads']['test_lea'],
                                                                            report_code=ods, 
                                                                            dry_run=False), 
                                                pd.DataFrame))
                except:
                    if self.cp.driver.service.is_connectable():
                        self.cp.driver.quit()
                    raise
