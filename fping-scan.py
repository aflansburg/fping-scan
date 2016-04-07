__author__ = 'misaflansb'

'''

fping -a -q -g <ip_addr>
           -a = alive hosts
           -q = quiet
           -g = address + mask (for scanning subnets)

'''

import os, sys # import system goodies
import time # this is for timing the subnet ping scan
import csv # for writing out the ip addresses that are up

# Uncomment this for scanning single subnets either by argument at command line or being prompted if no
# argument supplied -- also comment code labeled part 2 below

'''
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
'''

# Batch subnet operation -- comment this out and uncomment previous block and Part 2 as well

subnet_batch = ['10.30.1.0/24', '10.31.4.0/24', '10.31.94.0/23' '10.31.82.0/24', '10.31.83.0/24',
                '10.31.84.0/24', '10.66.0.0/24', '192.168.112.0/24', '192.168.113.0/24',
                '192.168.114.0/24', '192.168.115.0/24', '192.168.116.0/24', '192.168.118.0/24',
                '192.168.119.0/24', '192.168.120.0/24', '192.168.121.0/24', '172.16.1.0/24',
                '172.16.2.0/24', '172.16.3.0/24', '172.16.4.0/24', '172.16.5.0/24', '172.16.6.0/24',
                '172.16.7.0/24', '172.16.8.0/24', '172.16.9.0/24', '172.16.10.0/24', '172.16.11.0/24',
                '172.16.12.0/24', '172.16.13.0/24', '172.16.14.0/24', '172.16.15.0/24', '172.16.16.0/24',
                '10.10.1.0/24']

print ("Current subnet batch contains {0} subnets".format(len(subnet_batch)) + "\nScanning multiple subnets"
                                                                        " often takes a good deal of time.")
addr_list = []

for subnet in subnet_batch:
    print ("Please wait while subnet {0} is scanned.".format(subnet))
    start = time.time()

    for addr in os.popen("fping -a -q -g " + subnet):
        addr = addr.rstrip('\n')
        addr_list.append(addr)

    end = time.time()
    start = int(start)
    end = int(end)

    print ("Time elapsed: {0}".format(end-start) + " seconds")

addr_list.sort()

with open("up_hosts.csv", "wb") as out_file:
    csv_writer = csv.writer(out_file)
    for e in addr_list:
        csv_writer.writerow([e])

print "IP addresses that were up were written to {0}.".format(out_file.name)
out_file.close()

print ("Total number of hosts up: {0}".format(len(addr_list)))