import time
import board
import pwmio
import rotaryio
from adafruit_motor import motor
import Encoder as enc
from simple_pid import PID
import encodedMotor as em

# Motor Right
encR = enc.encoder(a=board.GP26, b=board.GP27, ticks=144)
mR = em.EncodedMotor(encR, board.GP8, board.GP9, "Motor Right", False)

# Motor Left
encL = enc.encoder(a=board.GP16, b=board.GP17, ticks=144)
mL = em.EncodedMotor(encL, board.GP10, board.GP11, "Motor Left", True)

mL.setEffort(1)
mR.setEffort(1)

turns = 4
straight = 5
rotationsToTurn = .78
while turns > 0:
    print(turns)
    turns -= 1

    ## Straight
    while ((mL.getPos() + mR.getPos())/2) < straight:
        if mL.getPos() > mR.getPos():
            mL.setEffort(0)
            mR.setEffort(1)
        else:
            mL.setEffort(1)
            mR.setEffort(0)
    mL.setPos()
    mR.setPos()

    ## Turn
    while ((- mL.getPos() + mR.getPos())/2) < rotationsToTurn:
        if -mL.getPos() > mR.getPos():
            mL.setEffort(0)
            mR.setEffort(1)
        else:
            mL.setEffort(-1)
            mR.setEffort(0)
    mL.setPos()
    mR.setPos()

while False:
    print("Enc 1 " + str(mL.getPos()) + " Enc 2 " + str(mR.getPos()))
    time.sleep(.1)

speed = .3
startTime = time.monotonic() - .001
while False:
    timeDelta = (time.monotonic() - startTime)
    #print("StartTime " + str(startTime))

    # print("mL")
    # print(((mL.getPos() / timeDelta),))
    if ((mL.getPos() / timeDelta) < speed):
        mL.setEffort(1)
    else:
        mL.setEffort(0)

    # print("mR")
    # print(((mR.getPos() / timeDelta),))
    if ((mR.getPos() / timeDelta) < speed):
        mR.setEffort(1)
    else:
        mR.setEffort(0)

    # print("Enc L " + str(mL.getPos()) + " Enc R " + str(mR.getPos()))
    # print("TimeDelta: " + str(timeDelta))
    time.sleep(.001)

speedArr = (0,0,0,0,0,0,0,0)
while True:
    prevPos = mL.getPos()
    prevTime = time.monotonic()
    time.sleep(.03)
    currSpeed = (mL.getPos() - prevPos)/(time.monotonic() - prevTime)

    speedArr.pop(0)
    speedArr.append(currSpeed)
    average = sum(speedArr) / len(speedArr)

    #print(str(round(average, 3)) + "  " + str(len(speedArr)) + "  Current Speed   " + str(currSpeed))

    print((average,sp, motor2.throttle))
    #print((motor2.throttle,))

    # Compute new output from the PID according to the systems current value
    pidOut = pid(average)
    mL.throttle = max(-1, min(pidOut, 1))

    #print("  Current Speed   " + str(currSpeed) + "  Current Throttle:    " + str(motor2.throttle))

while False:
    time.sleep(.01)
    error = enc1.getPos() - target

    motor1.throttle = max(min(3, 1), -1)
    print(enc1.getPos())

print("reset encoder")
enc2.setPos()

while enc2.getPos() < 10000:
    time.sleep(.01)
    print(enc2.getPos())
