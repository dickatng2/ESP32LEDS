# version 21
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
import sys
import network
import urequests
import os
import json
import ntptime

from ota import OTAUpdater
from wifi_config import SSID, PASSWORD
firmware_url = "https://github.com/dickatng2/ESP32LEDS/"

#ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

pwm = [22,23,21,19,27,12,14,26]
len_pwm = len(pwm)

duur = 0.3
pwm[0] = machine.PWM(Pin(12, Pin.OUT))
pwm[1] = machine.PWM(Pin(26, Pin.OUT))
pwm[2] = machine.PWM(Pin(14, Pin.OUT))
pwm[3] = machine.PWM(Pin(27, Pin.OUT))
pwm[4] = machine.PWM(Pin(19, Pin.OUT))
pwm[5] = machine.PWM(Pin(21, Pin.OUT))
pwm[6] = machine.PWM(Pin(22, Pin.OUT))
pwm[7] = machine.PWM(Pin(23, Pin.OUT))
 
def licht04(lengte, tijd):
    for i in range (len_pwm):
        pwm[i].duty(300)
        pwm[((i+1) % len_pwm)].duty(150)
        pwm[((i+2) % len_pwm)].duty(50)
        pwm[((i+1) % len_pwm)].duty(150)
        pwm[((i) % len_pwm)].duty(50)
        time.sleep(tijd)
        pwm[i].duty(0)
    time.sleep(0)
        
def timer_callback():
    from ota import OTAUpdater
    from wifi_config import SSID, PASSWORD

    firmware_url = "https://github.com/dickatng2/ESP32LEDS/"
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    print("callback")
    ota_updater.download_and_install_update_if_available()

def timer_test(a):
    timer_callback()
        
my_timer = Timer(0)
#my_timer.init(mode=Timer.PERIODIC, period=60000, callback=timer_test)
while True:
    licht04(len_pwm,duur)

