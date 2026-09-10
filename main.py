import os
import time
import sys
import io 
import numpy
import printer
from Skillset import * 
from Skill import * 
from Subs.Body import * 
from Subs.Cool import * 
from Subs.Intelligence import * 
from Subs.Reflexes import * 
from Subs.Technical_Ability import * 
#from VARS import * 
#from ollama import chat as MODEL
#from ollama import ChatResponse
#import datetime
#import pyfiglet
#import random


# output_buffer = io.StringIO()
# sys.stdout = output_buffer


import random
import time
import os
from colorama import Fore, Style, init
import threading
init()


printer.start()






perk_points = int(input("How many perk points do you have? "))
attribute_points = int(input("How many attribute points do you have? "))
build_type = input("What build type do you want (Technical Ability [TA], Reflexes, Body, Cool, Intelligence)? ")



