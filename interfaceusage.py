#!/usr/local/bin/python3.8
import os
INTERFACES = ['pppoe0']

speeds = {}

for interface in INTERFACES:
    results = address = os.popen("vnstat -tr -i {} | grep packets/s".format(interface)).read()
    while ("  " in results):
        results = results.replace("  ", " ")
    results = results.split(" ")
    if results[3] == "Mbit/s":
        speeds[interface] = {'rx':int(float(results[2])*1000000)}
    elif results[3] == "kbit/s":
        speeds[interface] = {'rx':int(float(results[2])*1000)}
    else:
        speeds[interface] = {'rx':int(results[2])}
    if results[8] == "Mbit/s":
        speeds[interface]['tx'] = int(float(results[7])*1000000)
    elif results[8] == "kbit/s":
        speeds[interface]['tx'] = int(float(results[7])*1000)
    else:
        speeds[interface]['tx'] = int(results[7])
    print('0 "Networkusage_{}" rx={}|tx={} Netzwerkauslastung {}'.format(interface, speeds[interface]['rx'], speeds[interface]['tx'], interface))
