# test
import machine, time
from machine import Pin, PWM, Timer
from time import sleep
led23 = Pin(23, Pin.OUT)
pwm = machine.PWM(led23)
t_slp = 1

def timer_callback():
    from ota import OTAUpdater
    from WIFI_CONFIG import SSID, PASSWORD

    firmware_url = "https://github.com/dickatng2/ESP32LEDS/"
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    ota_updater.download_and_install_update_if_available()

def timer_test(a):
    timer_callback()

def licht01():
    while True:
      pwm.duty(1023)
      time.sleep(t_slp)
      pwm.duty(700)
      time.sleep(t_slp)
      pwm.duty(500)
      time.sleep(t_slp)
      pwm.duty(200)
      time.sleep(t_slp)
      pwm.duty(100)
      time.sleep(t_slp)
      pwm.duty(50)
      time.sleep(t_slp)
      pwm.duty(10)
      time.sleep(t_slp)
      pwm.duty(5)
      time.sleep(t_slp)
        
my_timer = Timer(3)
my_timer.init(mode=Timer.PERIODIC, period=100000, callback=timer_test)
licht01
