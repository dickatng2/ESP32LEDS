# test
import machine, time
from machine import Pin, PWM
led23 = Pin(23, Pin.OUT)
pwm = machine.PWM(led23)
t_slp = 1
while True:
  pwm.duty(1023)
  time.sleep(t_slp)
  pwm.duty(500)
  time.sleep(t_slp)
  
