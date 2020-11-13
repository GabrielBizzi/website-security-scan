# -*- coding: utf-8 -*-
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from platform import python_version 
from tkinter import * 
from subprocess import call 
import subprocess 
import logging 
import time 
from requests import get
from socket import *
from subprocess import check_output
import os
import re

from searchLog import *

search = 'https://prcarmo.com.br'
Have_SSL='Continue'
dont_Have_SSL='Skip this step'

def check():
	datafile = file('sprint.txt')
	for line in datafile:
		if search in line:
			found = True
            
        else:
        	found = False
    return found

if check():
	print Have_SSL