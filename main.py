# version 60
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

pwm = [2]
len_pwm = len(pwm)
duur = 1  # 
per = 60000 # timer voor update via ota in msec

relais = Pin(26, Pin.OUT)
pwm[4] = machine.PWM(Pin(2, Pin.OUT))
            
def timer_test(a):
    ota_updater.download_and_install_update_if_available()
    print("callback")

def tijd():    
    print ("tijd")
    my_timer.init(mode=Timer.PERIODIC, period=per, callback=timer_test) 

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
tijd()

while True:    
    a = rtc.datetime()
    sec = a[6]
    minute = a[5]
    hh = a[4]
    if sec % 3 == 0:
       relais.value(1)
       pwm[0].duty(0)
       time.sleep(2)
       relais.value(0)
       pwm[0].duty(200)
       time.sleep(2)
   
