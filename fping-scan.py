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

start = time.time()

for addr in os.popen("fping -a -q -g 10.31.94.0/23"):
    if addr != '\n':
        addr_list.append(addr)
        print addr

end = time.time()
print ("Time elapsed: {0}".format(end-start) + " seconds")