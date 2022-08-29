from WPILib.WPILib import *

# drive straight for a set time period (defualt 1 second)
def drive_straight(driveTime: float = 1):
    drivetrain.setEffort(0.8, 0.8)
    time.sleep(driveTime)
    drivetrain.stop()

# drive at a slight counter clockwise arc for a set time period (default 1 second)
def arc_turn(turnTime: float = 1):
    drivetrain.setEffort(0.5, 0.8)
    time.sleep(turnTime)
    drivetrain.stop()

# turn CCW at a point for a set time period (default 1 second)
def point_turn(turnTime: float = 1):
    drivetrain.setEffort(-0.8, 0.8)
    time.sleep(turnTime)
    drivetrain.stop()

# pivot turn around the left wheel for a set time period (default 1 second)
def swing_turn(turnTime: float = 1):
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

# Approaches a wall at a set speed and then stops
def drive_till_close(targetDistance: float = 10.0):
    speed = 0.6
    while sonar.getDistance() > targetDistance:
        drivetrain.setEffort(speed, speed)
        time.sleep(0.01)
    drivetrain.setEffort(0, 0)

# Move to a certain distance from the wall
def standoff(targetDistance: float = 10.0):
    KP = 0.2
    while True:
        distance = sonar.getDistance()
        error = distance - targetDistance
        drivetrain.setEffort(error * KP, error*KP)
        time.sleep(0.01)

# Driving in a circle
def circle():
    while True:
        drivetrain.setEffort(0.6, 0.75)
