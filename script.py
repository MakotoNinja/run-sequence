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

sequence_id = app.find_sequence_by_name(name = s_name)

log = "Sequence Name: {}, Farmware Name: {}".format(s_name, f_name)
device.log(log, 'info', ['toast'])

device.execute(sequence_id)
