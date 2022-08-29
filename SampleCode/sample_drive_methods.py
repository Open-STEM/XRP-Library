from WPILib.WPILib import *

# drive straight for a set time period (defualt 1 second)
def drive_straight(drive_time: float = 1):
    drivetrain.set_effort(0.8, 0.8)
    time.sleep(drive_time)
    drivetrain.stop()

# drive at a slight counter clockwise arc for a set time period (default 1 second)
def arc_turn(turn_time: float = 1):
    drivetrain.set_effort(0.5, 0.8)
    time.sleep(turn_time)
    drivetrain.stop()

# turn CCW at a point for a set time period (default 1 second)
def point_turn(turn_time: float = 1):
    drivetrain.set_effort(-0.8, 0.8)
    time.sleep(turn_time)
    drivetrain.stop()

# pivot turn around the left wheel for a set time period (default 1 second)
def swing_turn(turn_time: float = 1):
    drivetrain.set_effort(0, 0.8)
    time.sleep(turn_time)
    drivetrain.stop()

#square function
def square(sidelength):
    for sides in range(4):
        drivetrain.go_straight(sidelength)
        drivetrain.go_turn(90)
    # Alternatively:
    # polygon(sidelength, 4)

#polygon function
def polygon(side_length, sides):
    for s in range(sides):
        drivetrain.go_straight(side_length)
        drivetrain.go_turn(360/sides)

# Driving in a circle
def circle():
    while True:
        drivetrain.set_effort(0.6, 0.75)
