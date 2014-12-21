#!/usr/bin/python
# This program is used to find the time of execution of python programs
# It is assumed the program is present in the current directory

import os
import time 

prgm_name = raw_input("Enter the filename of the program with .py extension: ")
start_time = time.time()
#exec '%s'%os.path.abspath(prgm_name)
os.system('python ' + prgm_name)
print("Your program executed in %s seconds" % str(time.time() - start_time))

