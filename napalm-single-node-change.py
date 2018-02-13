###############################################################################
# Task: Quick changes to a device with a diff so you can see what will be 
#       changed. 
#
# Usage: 'python napalm-single-node-change.py changes.txt'
#
# Results: The changes.txt file will get uploaded to the switch and then a 
#          a diff will occur and be presented to you. You will then have the
#          option to push the change or cancel it.
#
# Supports: python2.6+, napalm2.3
# 
# Author: Collin Clark
# Date: 10FEB2018
# Version: 1.0
################################################################################

from napalm import get_network_driver
import sys

driver = get_network_driver('ios')
device_ip = raw_input("Enter IP address of the host to make changes to: ")
device = driver(device_ip, 'USERNAME', 'PASSWORD')

# Get the CLI args
with open(sys.argv[1], 'r') as f:
    contents = f.read()

# Connect to the network device
print ("Connecting...")
device.open()

#print config_file
device.load_merge_candidate #(filename='changes.txt')

# Run a diff and present it
diffs = device.compare_config()
print ("+ means that the command will be added to the running config")
print ("- means that the command will be removed from the config")
print ("A blank means that there is a match between the file and the running config [no change]")
print ("")
print (diffs)

commit_config = raw_input("Do you want to commit the changes [Y or N]? ") 

if commit_config.lower() == 'y':
 print ("Commiting the configuration ...")
 device.commit_config()
 print ("Complete!")
 quit()

if commit_config.lower() == 'n':
 print ("OK, quitting the program...")
 quit()

else:
 print ("Quitting...")
 quit()
 
