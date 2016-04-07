__author__ = 'misaflansb'

'''

fping -a -q -g <ip_addr>
           -a = alive hosts
           -q = quiet
           -g = address + mask (for scanning subnets)

'''

import os
import time # this is for timing the subnet ping scan

subnet = raw_input("Enter the subnet to scan with CIDR mask (ex. 192.168.1.0/24): ")

addr_list = []

# For command counter
start = time.time()

for addr in os.popen("fping -a -q -g " + subnet):
    addr = addr.rstrip('\n')
    addr_list.append(addr)
    print addr

# Simple counter to calculate time to find up hosts
end = time.time()
start = int(start)
end = int(end)

print ("Time elapsed: {0}".format(end-start) + " seconds")
print ("Total number of hosts up in this subnet: {0}".format(len(addr_list)))