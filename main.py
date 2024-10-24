# test
import machine, time
from machine import Pin, PWM
from time import sleep
led23 = Pin(23, Pin.OUT)
pwm = machine.PWM(led23)
t_slp = 1
def timer_callback:
  test_ota.py

my_timer = Timer(id)
my_timer.init(mode=Timer.PERIODIC, period=100000, callback=timer_callback)

while True:
  pwm.duty(1023)
  time.sleep(t_slp)
  pwm.duty(700)
  time.sleep(t_slp)
  pwm.duty(500)
  time.sleep(t_slp)
  pwm.duty(200)
  time.sleep(t_slp)
