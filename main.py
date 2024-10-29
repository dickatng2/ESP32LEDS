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

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
pwm23 = machine.PWM(Pin(23,Pin.OUT))

led= []
led.append(pwm23)
leng = len(led)
def timer_callback():
    from ota import OTAUpdater
    from wifi_config import SSID, PASSWORD

    firmware_url = "https://github.com/dickatng2/ESP32LEDS/"
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    print("callback")
    ota_updater.download_and_install_update_if_available()

def timer_test(a):
    timer_callback()
    
def licht02():
  t_slp = 0.5
  led[0].duty(100)
  time.sleep(2)
  pwm23.duty(1023)
  time.sleep(t_slp)
  pwm23.duty(0)
  time.sleep(t_slp)

def licht03(lengte):
    for i in range (lengte):
        led[i].duty(500)
        time.sleep(1)

    
def licht01():
  t_slp = 1
  pwm23.duty(1023)
  time.sleep(t_slp)
  pwm23.duty(700)
  time.sleep(t_slp)
  pwm23.duty(500)
  time.sleep(t_slp)
  pwm23.duty(200)
  time.sleep(t_slp)
  licht02()
  pwm23.duty(100)
  time.sleep(t_slp)
  pwm23.duty(50)
  time.sleep(t_slp)
  pwm23.duty(10)
  time.sleep(t_slp)
  pwm23.duty(0)
  time.sleep(t_slp)

        
my_timer = Timer(0)
my_timer.init(mode=Timer.PERIODIC, period=20000, callback=timer_test)
while True:
    licht03(leng)
