#coding=utf-8
import random
import threading
from time import ctime,sleep
import json


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


def random_json():
    mac_data ={"mac": random_mac(), "rssi": random_rssi(), "range": random_range()}
    data_json = json.dumps(mac_data)
    print data_json


def random_id():
    return 1
threads = []

for i in range(1000):
    t = threading.Thread(target=random_json)
    threads.append(t)
if __name__ == '__main__':
    for i in range(1000):
        threads[i].setDaemon(True)
        threads[i].start()

    print "all over %s" %ctime()
# print random_mac()
# print random_rssi()
# print random_range()

# print random_json()