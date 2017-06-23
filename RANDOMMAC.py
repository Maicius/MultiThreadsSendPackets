#coding=utf-8

import random
import json
def random_mac():
    macList = []
    for i in range(1,7):
        randStr = "".join(random.sample("0123456789abcdef",2))
        macList.append(randStr)
    randMac = ":".join(macList)
    return randMac

probeList = []
def randomProbe(file, times):
    for i in range(1000):
        probe = {"id": i, "mmac": random_mac(), "rate": times, "wssid":"test", "wmac": random_mac()}
        probeList.append(probe)


file = open("/Users/maicius/代码/MultiThreadsSendPackets/probe.json", "w")
randomProbe(file, 3)
file.close()
