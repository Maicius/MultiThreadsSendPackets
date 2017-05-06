#coding=utf-8
import random
import threading
from time import ctime,sleep
import json
import urllib2

def random_mac():
    macList = []
    for i in range(1,7):
        randStr = "".join(random.sample("0123456789abcdef",2))
        macList.append(randStr)
    randMac = ":".join(macList)
    return randMac


def random_rssi():
    return random.randrange(-100, 0)


def random_range():
    return round(random.uniform(0, 100), 1)



def random_id():
    return random.randrange(1, 1000)


probeList = []


def randomProbe(times):

    for i in range(1000):
        probe = {"id": random_id(), "mmac": random_mac(), "rate": 3, "wssid": "test", "wmac": random_mac()}
        probes = json.dumps(probe)
        probeList.append(probes)


def random_json():
    headers = {'Content-Type': 'application/json'}

    probe = {"id": random_id(), "mmac": random_mac(), "rate": 3, "wssid": "test", "wmac": random_mac()}
    mac_data ={"mac": random_mac(), "rssi": random_rssi(), "range": random_range()}
    #data_json = json.dumps(mac_data)
    probe['data'] = mac_data
    probe = json.dumps(probe)
    print probe
    request = urllib2.Request(url='http://localhost:8080/upload.action', headers=headers, data=probe)
    response = urllib2.urlopen(request)


if __name__ == '__main__':
    threads = []
    probeList = []
    index=0
    # for i in range(1000):
    #     probe = {"id": i, "mmac": random_mac(), "rate": 3, "wssid": "test", "wmac": random_mac()}
    #     probes = json.dumps(probe)
    #     probeList.append(probes)

    for i in range(10000):
        t = threading.Thread(target=random_json)
        threads.append(t)
    for i in range(10000):
        threads[i].setDaemon(True)
        threads[i].start()

    print "all over %s" %ctime()
# print random_mac()
# print random_rssi()
# print random_range()

# print random_json()