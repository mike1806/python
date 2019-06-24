import socket, struct, dweepy, time, platform, random
#when you are connecting with the Pi
#from grovepi import *
#[temp, hum] = dht (port, 0)

def getTemp(): #cominig form Pi when you code it up
    #
    return random.randint(1,1000)


def getHumidity():
    return 10

def post(dic):
    thing='therapeutic-caption'
    #dweet.io
    print dweepy.dweet_for(thing, dic)

def getReadings():
    dict= {}
    dict["temperature"] = getTemp();
    dict["humidity"] = getHumidity()
    return dict

while True
    dict = getReadings();
    post(dict)
    time.sleep(5)