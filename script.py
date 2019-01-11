#!/usr/bin/env python

'''
 ' Testing running sequences and Farmwares
'''

import os
from farmware_tools import device
from farmware_tools import app
from farmware_tools import get_config_value

s_name = get_config_value('Random Move Relative', 'sequence_name')
f_name = get_config_value('Random Move Relative', 'farmware_name')

log = "Sequence Name: {}, Farmware NName: {}".format(s_name, f_name)
device.log(log, 'info', ['toast'])
