#!/usr/bin/env python

'''
 ' Testing running sequences and Farmwares
'''

import os
from farmware_tools import device
from farmware_tools import app
from farmware_tools import get_config_value

s_name = str(get_config_value('Run Sequence', 'sequence_name'))
f_name = str(get_config_value('Run Sequence', 'farmware_name'))

log = "Sequence Name: {}, Farmware Name: {}".format(s_name, f_name)
device.log(log, 'info', ['toast'])
