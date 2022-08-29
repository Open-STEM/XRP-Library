import time
from WPILib.WPILib import *

"""
    File meant to help students test basic drive functionality.

    By the end of completing this file the student's robot should
    have the robot driving straight and turning
"""

def test_drive():
    # Drive forward cm
    drivetrain.go_straight(25, 0.5)

    time.sleep(1)

    # turn 90 degrees clockwise
    drivetrain.go_turn(90,0.5)

    time.sleep(1)

    # turn 90 degrees counter clockwise by setting speed negative
    drivetrain.go_turn(90, -0.5)

    time.sleep(1)

    # drive backwards 25 cm by setting distance negative. s
    # There is no difference between setting speed or distance negative, both work
    drivetrain.go_straight(-25,0.5)

