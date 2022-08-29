import time
from WPILib.WPILib import *

"""
    File meant to help students test basic drive functionality.

    By the end of completing this file the student's robot should
    have the robot driving straight and turning after waiting for a button press.
"""

def testDrive():
    # Drive forward cm
    drivetrain.goStraight(25, 0.5)

    time.sleep(1)

    # turn 90 degrees clockwise
    drivetrain.goTurn(90,0.5)

    time.sleep(1)

    # turn 90 degrees counter clockwise by setting speed negative
    drivetrain.goTurn(90, -0.5)

    time.sleep(1)

    # drive backwards 25 cm by setting distance negative. s
    # There is no difference between setting speed or distance negative, both work
    drivetrain.goStraight(-25,0.5)

