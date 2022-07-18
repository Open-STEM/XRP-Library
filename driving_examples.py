from WPILib import *

#simeple turn
def simpleTurn():
    driveBase.setEffort(0.5, 0.8)

def pointTurn():
    driveBase.setEffort(-0.8, 0.8)

def swingTurn():
    driveBase.setEffort(0, 0.8)

#square function
def square(sidelength):
    for sides in range(4):
        driveBase.straight(sidelength)
        driveBase.turn(90)

#polygon function
def polygon(sides):
    for s in range(sides):
        driveBase.straight(150)
        driveBase.turn(360/sides)

def standoff():
    Kp = 0.2
    while True:
        distance = sonar.distance
        error = distance - 10.0
        driveBase.setEfforts(error * Kp)
        time.sleep(0.01)

def driveTillClose():
    while True:
        if sonar.distance > 10:
            driveBase.setEffort(0.60, 0.60)
        else:
            driveBase.setEffort(0, 0)
        time.sleep(0.01)

# Driving in a circle
def circle():
    while True:
        driveBase.setEffort(0.6, 0.75)

# Characterize line sensors
def checkLineSensors():
    while True:
        print("Left:", refl.left(), "Right:", refl.right())
        time.sleep(0.5)

# Drive to a line and stop
def driveToLineAndStop():
    driveBase.setEffort(0.6, 0.6)
    while refl.left() < 5 and refl.right() < 5:
        time.sleep(0.01)
    driveBase.setEffort(0, 0)

# Two sensor digital line tracking
def twoSensorLineTrack():
    while True:
        high = 0.75
        low = 0.4
        r = refl.right()
        l = refl.left()
        print ("Left:", l, "Right:", r)
        if (r > 5):
            driveBase.setEffort(high, low)
        elif (l > 5):
            driveBase.setEffort(low, high)
        else:
            driveBase.setEffort(high, high)
        time.sleep(0.01)

# Single sensor line tracking
def oneSensorLineTrack():
    while True:
        high = 0.75
        low = 0.4
        r = refl.right()
        if (r > 5):
            driveBase.setEffort(high, low)
        else:
            driveBase.setEffort(low, high)
        time.sleep(0.01)

def lineTrack():
    baseEffort = 0.6
    Kp = 0.02
    while True:
        error = refl.right() - refl.left()
        driveBase.setEffort(0.6 + error * Kp, 0.6 - error * Kp)

# see what 3/4 speed looks like
def speedTest():
    driveBase.setEffort(0.75, 0.75)

# drive 11" using timing
def drive11inches():
    print("Drive 11 inches")
    secondsPerInch = 0.2775
    driveBase.setEffort(0.75, 0.75)
    time.sleep(secondsPerInch * 11)
    driveBase.setEffort(0, 0)

def driveInchesTimed(inches):
    secondsPerInch = 0.2775
    driveBase.setEffort(0.75, 0.75)
    time.sleep(secondsPerInch * inches)
    driveBase.setEffort(0, 0)

def triangle():
    for sides in range(3):
        straight(200)
        turn(120)

def triangles():
    for step in range(12):
        triangle()
        turn(20)

def servo_test():

    pwm = pwmio.PWMOut(board.GP12, duty_cycle=2 ** 15, frequency=50)
    # Create a servo object, my_servo.
    my_servo = servo.Servo(pwm)

    while True:
        my_servo.angle = 0
        time.sleep(3)
        my_servo.angle = 70
        time.sleep(3)

    while True:
        print("going from 0 to 180")
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)
        print("going from 180 to 0")
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)

servo_test()

