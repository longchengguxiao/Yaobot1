# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:04:06 2021

@author: Lenovo
"""

import logging
import sys


_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(
    logging.Formatter('[%(asctime)s %(name)s] %(levelname)s: %(message)s')
)

logger = logging.getLogger('lucia')
logger.addHandler(_handler)
logger.setLevel(logging.INFO)