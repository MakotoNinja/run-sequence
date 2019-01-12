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
loops = get_config_value('Run Sequence', 'loop_farmware', int)

if len(''.join(s_name.split())) > 0:
	try:
		sequence_id = app.find_sequence_by_name(name = s_name)
	except:
		device.log("Couldn't find a sequence with name: {}".format(s_name), 'error', ['toast'])
else :
	device.log("No text was entered in sequence input.", 'error', ['toast'])

if len(''.join(f_name.split())) > 0:
	for i in range(loops):
		device.execute_script(label = f_name)
else :
	device.log("No text was entered in farmware input.", 'error', ['toast'])

# device.execute(sequence_id)
