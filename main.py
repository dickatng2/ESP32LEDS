# version 28
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
import sys
import network
import urequests
import os
import json

from us import HCSR04
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=30000)

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
firmware_url = "https://github.com/dickatng2/ESP32LEDS/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

pwm = [22,23,21,19,27,12,10,26,25,33,32]
len_pwm = len(pwm)
duur = 0.1 

pwm[0] = machine.PWM(Pin(26, Pin.OUT)) 
pwm[1] = machine.PWM(Pin(13, Pin.OUT))
pwm[2] = machine.PWM(Pin(27, Pin.OUT))
pwm[3] = machine.PWM(Pin(14, Pin.OUT))
pwm[4] = machine.PWM(Pin(2, Pin.OUT))
pwm[5] = machine.PWM(Pin(15, Pin.OUT))
pwm[6] = machine.PWM(Pin(23, Pin.OUT))
pwm[7] = machine.PWM(Pin(25, Pin.OUT))
pwm[8] = machine.PWM(Pin(33, Pin.OUT))
pwm[9] = machine.PWM(Pin(12, Pin.OUT))
pwm[10] = machine.PWM(Pin(04, Pin.OUT))             
 
def licht04(lengte, tijd):                                        
    for i in range (lengte):    
        pwm[i].duty(1023)
        pwm[((i+5) % len_pwm)].duty(600)
        pwm[((i+4) % len_pwm)].duty(400)
        pwm[((i+3) % len_pwm)].duty(100)
        pwm[((i+2) % len_pwm)].duty(0)
        time.sleep(tijd)
    
def licht05(tijd):
    for i in range (11):
        print (i)
        pwm[i].freq(50)
        pwm[i].duty(1023)
        pwm[11-i].duty(1023)
        time.sleep(tijd)
        pwm[i].duty(0)
        pwm[11-i].duty(0)
        wait(3)
        
def timer_callback():
#    firmware_url = "https://github.com/dickatng2/ESP32LEDS/"
#    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    print("callback")
    ota_updater.download_and_install_update_if_available()

def timer_test():
    timer_callback()

def tijd():
    my_timer = Timer(0)
    my_timer.init(mode=Timer.PERIODIC, period=20000, callback=timer_test) 

tijd()
cnt = 0
while True:    
     cnt += 1
     #licht04(len_pwm, duur)
     print (cnt)
     sleep(1)

