import dweepy
import time
import psutil
import random
import datetime
import grovepi
import math
import sqlite3
import requests
import json

#import config


try:
    import configparser
except ImportError:
    # Python 2.x fallback
    import ConfigParser as configparser


'''
written by Michal Borkowski

'''

'''
Modified Code
replaced reading config from config.py to config.ini
thing = config.thing
th_port = config.th_port
red_led = config.red_port
blue_led = config.blue_port
switch_port = config.switch_port
analog_pot=0
'''

#config.ini
config = configparser.ConfigParser(allow_no_value=True)
config.read('config.ini')
config.sections()
if 'dweet' not in config:
        print('dweetName not found')
        exit()

dweetName = config.get('dweet', 'dweetName')
print('dweetName',dweetName)

if 'dexter' not in config:
        print('port configs not found')
        exit()

conn = sqlite3.connect('database.db')
c = conn.cursor()

#Dweet.io
dweetIO = "https://dweet.io/dweet/for/"
myName = dweetName
temperatureKey = "Temperature"
redKey = "Red"
switchKey = "Switch"
analogKey = "Analog"

#read port configuration for sensors set in config.ini

th_port = int(config.get('dexter', 'th_port'))
red_led = int(config.get('dexter', 'red_port'))
switch_port = int(config.get('dexter', 'switch_port'))
analog_pot = int(config.get('dexter', 'analog_pot'))

url = 'https://dweet.io/dweet/for/mike_ca'
# temp humidity sensor there are two types blue and white
blue=0
white=1
# init value for onoff set to 0
onoff=0;

scale=0.1

# my methods
def get_Hum_Temp():
        ans = grovepi.dht(th_port,blue)
        print("Temperature =", th_port)
        # returns a list [temp, humidity]
        return ans

def getTime():
        now = datetime.datetime.now()
        return ("%d:%02d:%02d" % (now.hour,now.minute,now.second))

def switchRed(onoff):
        print(red_led,onoff)
        grovepi.digitalWrite(red_led,onoff)
        pass

def switchBlue(onoff):
        grovepi.digitalWrite(blue_led,onoff)
        pass

def switchGreen(onoff):
        grovepi.digitalWrite(green_led,onoff)
        pass

def readLogic(pin):
        btn = grovepi.digitalRead(pin)
        print(btn)
        return btn;

def setPinMode(pin,mode):
        grovepi.pinMode(pin,mode)
        pass

def analogRead(pin):
        return grovepi.analogRead(pin)

def checkHighTemp(temp,level):
        level=level*scale
        #compares the values temp/level of pot
        print(str(temp) +" : "+str(level))
        if(temp >= level):
                switchRed(1)
                hiTemp = 1
        else:
                switchRed(0)
                hiTemp = 0
        return hiTemp


def getReadings():
        timenow=getTime()
        print('timenow')
        # get output from temp and humidity sensor
        list_temp_hum = get_Hum_Temp()
        # assign temp
        temp = list_temp_hum[0]
        # assign humidity
        hum= list_temp_hum[1]
        # read output from switch
        digitalIP= readLogic(switch_port)

        level = analogRead(analog_pot)
        #compares temp from temp humidity sensor with level of pot
        hiTemp = checkHighTemp(temp,level)


        # assigns the values for pi storage
        demo(timenow, temp, hum, digitalIP)
        dict = {}
        #adding data to pi dictionary
        #data comes from my methods()
        dict['Time'] = timenow
        dict['Temperature'] = temp
        dict['Humidity'] = hum
        dict['Button'] = digitalIP
        dict['High_Temp'] = hiTemp

        return dict

def post(dict):
        thing = 'mike_ca'
        print dweepy.dweet_for(thing,dict)
        pass

def get_info():
        print("___________________________________________________________")
        print('Sensors should be connected to following:' )
        print('temp and humidity sensor: PORT D'+str(th_port))
        print('the red  led sensor: PORT D'+str(red_led))
        print('the analog pot sensor: PORT A'+str(analog_pot))
        print('push button switch sensor: PORT D'+str(switch_port))
        print("___________________________________________________________")
        pass


# Save to pi DB
def demo(a, b, x, d):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO readings VALUES(?,?,?,?)',(a, b, x, d))
        conn.commit()
        conn.close()


# indicates ports for use
temperatureString = dweetIO+myName+'?'+temperatureKey+str(th_port)
print(temperatureString)
rqs = requests.get(temperatureString)

redString = dweetIO+myName+'?'+redKey+'='+str(red_led)
print(redString)
rqs3 = requests.get(redString)

switchString = dweetIO+myName+'?'+switchKey+'='+str(switch_port)
print(switchString)
rqs3 = requests.get(switchString)

analogString = dweetIO+myName+'?'+analogKey+'='+str(analog_pot)
print(analogString)
rqs3 = requests.get(analogString)

conn.close()

#initilize

def initBoard():
        get_info()
        #switch off red led
        switchRed(1)
        # set push button switch to type INPUT
        switch_port=3
        mode = "INPUT"
        setPinMode(switch_port,mode)
        print('init complete')
        pass


        while True:
                print('get readings')

                try:
                        dict = getReadings()
                        print(dict)
                        post(dict)
                        time.sleep(10)

                except IOError:
                        print("Error IOException")

                except KeyboardInterrupt:
                        exit()


initBoard()
runCode()

