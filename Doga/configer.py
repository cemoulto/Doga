# -*- coding: utf-8 -*-

"""
Doga.configer

This module gives other modules access to use configuration values
"""

import os
from ConfigParser import SafeConfigParser

config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config_file = os.path.abspath(config_file_path)

parser = SafeConfigParser()
parser.read(config_file)


def value(key):
    """ return config value for key

    param: key(str) : config data key
    """

    return parser.get('Doga', key)
