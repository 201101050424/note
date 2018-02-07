# encoding=utf-8
import sys
import argparse
import re
import os
import datetime
import logging
import logging.handlers
import redis
import traceback
import operator
import requests
import bisect
import json
import hashlib
import random
import inspect
import itertools
import numpy
from operator import itemgetter
from tqdm import *
from subprocess import Popen
from subprocess import PIPE
from threading import Lock
from threading import Thread
from urllib import urlencode
from Queue import Queue

logger = logging.getLogger('logger')
if logger.handlers == []:
    formatter = logging.Formatter(
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging.NOTSET)
    logger.addHandler(handler)

    log_file = os.path.basename(__file__).split('.')[0] + '_log'
    handler = logging.FileHandler(filename=log_file, mode='w')
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)


if __name__ == "__main__":
    s = 'abcd123efg'
    logger.debug(re.sub('[^a-zA-Z]', '', s))
