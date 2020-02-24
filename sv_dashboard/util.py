"""sv_dashboard Utility methods
"""
import os
import yaml
import logging
import csv
from pathlib import Path


def load_config():
    """Load conf file defined by ENV var SV_DASHBOARD_CONF.
    If not available load ./conf.yaml
    """
    config = {}
    try:
        cfg_file = os.environ.get('SV_DASHBOARD_CONF')
        if not cfg_file:
            cfg_file = os.getcwd() + '/conf.yml'
            logging.warning('using default configuration from %s', cfg_file)
        with open(cfg_file, 'rt') as cfg:
            config = yaml.safe_load(cfg.read())
            logging.debug('config=%s', config)
    except IOError:
        logging.error('Error loading configuration', exc_info=1)
    return config


def get_data():
    return
