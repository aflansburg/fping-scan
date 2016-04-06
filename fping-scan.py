__author__ = 'misaflansb'

'''

fping -a -q -g <ip_addr>
           -a = alive hosts
           -q = quiet
           -g = address + mask (for scanning subnets)

'''

import os
import time # this is for timing the subnet ping scan

addr_list = []

# For command counter
start = time.time()

for addr in os.popen("fping -a -q -g 10.31.94.0/23"):
    addr = addr.rstrip('\n')
    addr_list.append(addr)
    print addr

# Simple counter to calculate time to find up hosts
end = time.time()
start = int(start)
end = int(end)

print ("Time elapsed: {0}".format(end-start) + " seconds")
print ("Total number of hosts up in this subnet: {0}".format(len(addr_list)))