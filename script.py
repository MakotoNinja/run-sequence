#!/usr/bin/env python

'''
 ' Testing running sequences and Farmwares
'''

import os
import requests
from farmware_tools import device
from farmware_tools import app
from farmware_tools import get_config_value

TOKEN =
headers = {'Authorization': 'Bearer {}'.format(api_token), 'content-type': "application/json"}

s_name = get_config_value('Run Sequence', 'sequence_name')
f_name = 'two'#get_config_value('Run Sequence', 'farmware_name')

log = "Sequence Name: {}, Farmware Name: {}".format(s_name, f_name)
device.log(log, 'info', ['toast'])
