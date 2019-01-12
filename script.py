#!/usr/bin/env python

'''
 ' Testing running sequences and Farmwares
'''

import os
import json
import requests

from farmware_tools import device, app
from farmware_tools import get_config_value

s_name = get_config_value('Run Sequence', 'sequence_name', str)
f_name = get_config_value('Run Sequence', 'farmware_name', str)

if len(''.join(s_name.split())) > 0:
	try:
		sequence_id = app.find_sequence_by_name(name = s_name)
	except:
		device.log("Couldn't find a sequwnce name: {}".format(s_name), 'error', ['toast'])
else :
	device.log("No text was entered.", 'error', ['toast'])
#device.execute(sequence_id)
