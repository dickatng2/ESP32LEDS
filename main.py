# version 20
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
import sys
import network
import urequests
import os
import json
import ntptime

led = []
for i in range (23):
    led.append(machine.PWM(Pin(i,Pin.OUT)))

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
firmware_url = "https://github.com/dickatng2/ESP32LEDS/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

led[0].init


def timer_callback():
#     from ota import OTAUpdater
#     from WIFI_CONFIG import SSID, PASSWORD
# 
#     firmware_url = "https://github.com/dickatng2/ESP32LEDS/"
#     ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    ota_updater.download_and_install_update_if_available()

def timer_test(a):
    timer_callback()

def licht01():
  t_slp = 0.5
  pwm23.duty(1023)
  time.sleep(t_slp)
  pwm23.duty(700)
  time.sleep(t_slp)
  pwm23.duty(500)
  time.sleep(t_slp)
  pwm23.duty(200)
  time.sleep(t_slp)
  pwm23.duty(100)
  time.sleep(t_slp)
  pwm23.duty(50)
  time.sleep(t_slp)
  pwm23.duty(10)
  time.sleep(t_slp)
  pwm23.duty(0)
  time.sleep(t_slp)
  pwm22.duty(1023)
  time.sleep(t_slp)
  pwm22.duty(700)
  time.sleep(t_slp)
  pwm22.duty(500)
  time.sleep(t_slp)
  pwm22.duty(200)
  time.sleep(t_slp)
  pwm22.duty(100)
  time.sleep(t_slp)
  pwm22.duty(50)
  time.sleep(t_slp)
  pwm22.duty(10)
  time.sleep(t_slp)
  pwm22.duty(0)
  time.sleep(t_slp)
        
my_timer = Timer(0)
my_timer.init(mode=Timer.PERIODIC, period=20000, callback=timer_test)
