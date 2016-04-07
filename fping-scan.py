__author__ = 'misaflansb'

'''

fping -a -q -g <ip_addr>
           -a = alive hosts
           -q = quiet
           -g = address + mask (for scanning subnets)

'''

import os, sys # import system goodies
import time # this is for timing the subnet ping scan

# input subnet as argument

if len(sys.argv) == 2:
    subnet = str(sys.argv[1])

else:
    subnet = raw_input("Enter the subnet to scan with CIDR mask (ex. 192.168.1.0/24): ")

addr_list = []

# For command counter
print ("Please wait while subnet {0} is scanned.".format(subnet))
start = time.time()

for addr in os.popen("fping -a -q -g " + subnet):
    addr = addr.rstrip('\n')
    addr_list.append(addr)

# sort ip addresses descending and print
addr_list.sort()
for ip in addr_list:
    print ip

# Simple counter to calculate time to find up hosts
end = time.time()
start = int(start)
end = int(end)

print ("Time elapsed: {0}".format(end-start) + " seconds")
print ("Total number of hosts up in this subnet: {0}".format(len(addr_list)))