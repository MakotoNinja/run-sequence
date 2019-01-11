#!/usr/bin/env python

'''
 ' Testing running sequences and Farmwares
'''

import os
import requests
from farmware_tools import device
from farmware_tools import app
from farmware_tools import get_config_value

try:
	api_token = os.environ['API_TOKEN']
except KeyError:
	api_token = 'Not Set'
	device.log('API_TOKEN not set', message_type='error', title='Class API:api_setup')

#headers = {'Authorization': 'Bearer {}'.format(api_token), 'content-type': "application/json"}

s_name = get_config_value('Run Sequence', 'sequence_name', str)
f_name = get_config_value('Run Sequence', 'farmware_name', str)

log = "Sequence Name: {}, Farmware Name: {}".format(s_name, f_name)
device.log(log, 'info', ['toast'])
