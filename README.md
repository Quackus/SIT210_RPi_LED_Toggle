# SIT210_RPi_LED_Toggle

import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(7,RPi.GPIO.OUT)

while 1:
    RPi.GPIO.output(7,RPi.GPIO.HIGH)
    time.sleep(0.1)
    RPi.GPIO.output(7,RPi.GPIO.LOW)
    time.sleep(0.1)
