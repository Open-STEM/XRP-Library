import time
import board
import adafruit_hcsr04

# Ultrasonic Rangefinder
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP28, echo_pin=board.GP7)
while False:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)
