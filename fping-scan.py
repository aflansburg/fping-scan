__author__ = 'misaflansb'

'''
## Fping Usage

fping -a -q -g <ip_addr>
           -a = alive hosts
           -q = quiet
           -g = address + mask (for scanning subnets)
'''

import os, sys # import system goodies
import time # this is for timing the subnet ping scan
import csv # for writing out the ip addresses that are up
import re # regex

# Batch subnet operation

subnet_batch = ['10.30.1.0/24', '10.31.4.0/24', '10.31.94.0/23' '10.31.82.0/24', '10.31.83.0/24',
                '10.31.84.0/24', '10.66.0.0/24', '192.168.112.0/24', '192.168.113.0/24',
                '192.168.114.0/24', '192.168.115.0/24', '192.168.116.0/24', '192.168.118.0/24',
                '192.168.119.0/24', '192.168.120.0/24', '192.168.121.0/24', '172.16.1.0/24',
                '172.16.2.0/24', '172.16.3.0/24', '172.16.4.0/24', '172.16.5.0/24', '172.16.6.0/24',
                '172.16.7.0/24', '172.16.8.0/24', '172.16.9.0/24', '172.16.10.0/24', '172.16.11.0/24',
                '172.16.12.0/24', '172.16.13.0/24', '172.16.14.0/24', '172.16.15.0/24', '172.16.16.0/24',
                '10.10.1.0/24']

# small subnet_batch for testing
# subnet_batch = ['10.66.0.0/24', '10.10.1.0/24']

print ("Current subnet batch contains {0} subnets".format(len(subnet_batch)) + "\nScanning multiple subnets"
                                                                        " often takes a good deal of time.")
addr_list = []

for subnet in subnet_batch:
    print ("Please wait while subnet {0} is scanned.".format(subnet))
    start = time.time()

    for response in os.popen("fping -a -q -g " + subnet):
        response = response.rstrip('\n')
        addr_list.append(response)

    end = time.time()
    start = int(start)
    end = int(end)

    print ("Time elapsed: {0}".format(end-start) + " seconds")

addr_list.sort()
subnet_list = {}

with open("up_hosts.csv", "wb") as out_file:
    csv_writer = csv.writer(out_file)
    for address in addr_list:
        csv_writer.writerow([address])

for address in addr_list:
    # subnet capture
    regex = r'(\d{2,3}.\d{1,3}.\d{1,3})'
    g = re.search(regex, address, re.IGNORECASE)

    # record subnet if not in dict already, and increment if it is

    if g.group(1) not in subnet_list:
        subnet_list[g.group(1)] = 1
    else:
        subnet_list[g.group(1)] += 1


print "IP addresses that were up were written to {0}.".format(out_file.name)
out_file.close()

print "Total number of hosts up: {0}".format(len(addr_list))

for k, v in subnet_list.iteritems():
    print "Subnet {0} currently has {1} hosts up.".format(k, v)
