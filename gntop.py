#!/usr/bin/python
import psutil as ps
import sys
import time

# Function to convert bytes to human readable fromat
def bytesTohuman(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        tp = (i*10) + 10
        prefix[s] = 2**tp

    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return "%.2f %s" % (value, s)

# Use psutil to read network bytes received and transmitted.
network_tx = ps.net_io_counters(pernic=True)
NIC_Names = list(network_tx.keys())
# Sort Network Names based on the TX and RX
NIC_Names.sort(key=lambda x: sum(network_tx[x]), reverse=True)
for nic in NIC_Names:
    network_before = ps.net_io_counters(pernic=True)
    total_bw_before = network_before[nic][0] + network_tx[nic][1]
    time.sleep(1)
    network_after = ps.net_io_counters(pernic=True)
    total_bw_after = network_after[nic][0] + network_tx[nic][1]
    bw_per_second = bytesTohuman(total_bw_after - total_bw_before)
    print("NIC Name: %s" % nic)
    print("Total Bandwidth Usage:  %s" % bw_per_second, end='\n')
    print("\n")
