__author__ = 'misaflansb'

'''

fping -a -q -g <ip_addr>
           -a = alive hosts
           -q = quiet
           -g = address + mask (for scanning subnets)

'''

import os

addr_list = []

for addr in os.popen("fping -a -q -g 10.31.94.0/23"):
    addr_list.append(addr)
    print addr