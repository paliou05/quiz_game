# -*-coding: utf8-*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from datetime import datetime
import sys


if sys.version_info[0] < 3:
    input = raw_input
class SecondCounter(object):
    def __init__(self):
        self.start_time = None
    def start(self):
        self.start_time = datetime.now()
    @property
    def value(self):
        return (datetime.now() - self.start_time).total_seconds()
    def peek(self):
        return self.value
    def finish(self):
        return self.value
