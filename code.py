import time
from analogio import AnalogIn
import digitalio
import board
import pwmio
import rotaryio
from adafruit_motor import motor
import Encoder as enc
from simple_pid import PID
import encodedMotor as em
import drive as drv
import adafruit_hcsr04

# Motor Right
encR = enc.encoder(a=board.GP2, b=board.GP3, ticks=144)
mR = em.EncodedMotor(encR, board.GP8, board.GP9, "Motor Right", False)

# Motor Left
encL = enc.encoder(a=board.GP4, b=board.GP5, ticks=144)
mL = em.EncodedMotor(encL, board.GP10, board.GP11, "Motor Left", True)

mL.setEffort(0)
mR.setEffort(0)

lRfl = AnalogIn(board.A1) #GP27
rRfl = AnalogIn(board.A0) #GP26

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP28, echo_pin=board.GP7)

midEffort = 0.6
errorCap = 1 - midEffort
error = 0
kp = 20/100000

while False:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)

while True:
    rL = lRfl.value
    rR = rRfl.value

    error = -(rL - rR)
    e = min(errorCap , max(-errorCap, error * kp))

    if e < .15:
        me = .84
    else:
        me = midEffort

    mL.setEffort(me + e)
    mR.setEffort(me - e)

    if True:
        time.sleep(.1)
        print("Left Reflectance     " + str(rL))
        print("Right Reflectance    " + str(rR))
        print(e)

mL.setEffort(0)
mR.setEffort(0)

def tof_mm(time_of_flight):
    """
    EZ1 ultrasonic sensor is measuring "time of flight"
    Converts time of flight into distance in centimeters
    """
    convert_to_mm = 5.8
    cm = time_of_flight / convert_to_mm
