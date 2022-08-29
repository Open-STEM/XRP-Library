from WPILib.WPILib import *

#drive straight 100 cm
def driveStraight(driveTime: float = 1):
    drivetrain.setEffort(0.8, 0.8)
    time.sleep(driveTime)
    drivetrain.stop()

def arcTurn(turnTime: float = 1):
    drivetrain.setEffort(0.5, 0.8)
    time.sleep(turnTime)
    drivetrain.stop()

def pointTurn(turnTime: float = 1):
    drivetrain.setEffort(-0.8, 0.8)
    time.sleep(turnTime)
    drivetrain.stop()

def swingTurn(turnTime: float = 1):
    drivetrain.setEffort(0, 0.8)
    time.sleep(turnTime)
    drivetrain.stop()

#square function
def square(sidelength):
    for sides in range(4):
        drivetrain.goStraight(sidelength)
        drivetrain.goTurn(90)
    # Alternatively:
    # polygon(sidelength, 4)

#polygon function
def polygon(sidelength, sides):
    for s in range(sides):
        drivetrain.goStraight(sidelength)
        drivetrain.goTurn(360/sides)

# Move to a certain distance from the wall
def standoff(targetDistance: float = 10.0):
    KP = 0.2
    while True:
        distance = sonar.getDistance()
        error = distance - targetDistance
        drivetrain.setEffort(error * KP, error*KP)
        time.sleep(0.01)

def driveTillClose(targetDistance: float = 10.0):
    speed = 0.6
    while True:
        if sonar.getDistance() > targetDistance:
            drivetrain.setEffort(speed, speed)
        else:
            drivetrain.setEffort(0, 0)
            break
        time.sleep(0.01)

# Driving in a circle
def circle():
    while True:
        drivetrain.setEffort(0.6, 0.75)
