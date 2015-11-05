#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 by Christian Tremblay, P.Eng <christian.tremblay@servisys.com>
#
# Licensed under LGPLv3, see file LICENSE in this source tree.
"""
Change Fan status based on Fan Command
"""

from .TaskManager import Task
from random import randint


class Match(Task):
    """
    Will fit fan status with fan command
    """

    def __init__(self, command = None, status = None, delay=5):        
        self.command = command
        self.status = status
        Task.__init__(self, delay=(delay+randint(0,9)/10))

    def task(self):
        self.status._setitem(self.command.value)        
        
    def beforeStop(self):
        self.status = 'auto'
