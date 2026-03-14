# version 72
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
import sys
import network
import urequests
import os
import json

rtc = machine.RTC()

from ota import OTAUpdater
from wifi_config import SSID, PASSWORD

firmware_url = "https://github.com/dickatng2/ESP32LEDS/"
my_timer = Timer(4)

relais_1 = Pin(26, Pin.OUT)
pwm[0] = machine.PWM(Pin(2, Pin.OUT))
            
def timer_test(a):
    ota_updater.download_and_install_update_if_available()
    print("callback")

def tijd():    
    print ("tijd")
    my_timer.init(mode=Timer.PERIODIC, period=6000, callback=timer_test) 

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
tijd()

while True:    
    a = rtc.datetime()
    if a[6] % 3 == 0: 
        start_1 = True
            while start_1:
                relais_1.value(1)                
        pwm[0].duty(0)
        time.sleep(2)
        start_1 = False        
        
        relais_1.value(0)
        pwm[0].duty(100)
        time.sleep(2)
   
