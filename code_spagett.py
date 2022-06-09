import time
from analogio import AnalogIn
import digitalio
import board
import pwmio
import rotaryio
from adafruit_motor import motor
import encoder as enc
from simple_pid import PID
import encoded_motor as em
import drive as drv
import adafruit_hcsr04

# Motor Left
encL = enc.encoder(a=board.GP4, b=board.GP5, ticksPerRev=144)
mL = em.encoded_motor(encL, board.GP8, board.GP9, "Motor Left", True)

# Motor Right
encR = enc.encoder(a=board.GP2, b=board.GP3, ticksPerRev=144, doFlip = True)
mR = em.encoded_motor(encR, board.GP10, board.GP11, "Motor Right")

# Drive Base
driveBase = drv.drive(mL,mR)


midEffort = 0.6
errorCap = 1 - midEffort
error = 0
kp = 20/100000

#Test Drive
while False:
    driveBase.setEffort(1,1)
    print()
    print(mL)
    print(mR)
    time.sleep(2)

# Ultrasonic Rangefinder
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP28, echo_pin=board.GP7)
while False:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)

# Line Follower
lRfl = AnalogIn(board.A1) #GP27
rRfl = AnalogIn(board.A0) #GP26

while True:
    rL = lRfl.value
    rR = rRfl.value

    error = -(rL - rR)
    e = min(errorCap , max(-errorCap, error * kp))

    if e < .15:
        me = .84
    else:
        me = midEffort

    driveBase.setEffort(leftEffort = me + e, rightEffort = me - e)

    if True:
        print("Left Effort  : " + str(me+e))
        print("Right Effort : " + str(me-e))

    if False:
        time.sleep(.1)
        print("Left Reflectance     " + str(rL))
        print("Right Reflectance    " + str(rR))
        print(e)
