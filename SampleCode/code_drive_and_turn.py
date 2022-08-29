import time
import WPILib.WPILib as robot

"""
    File meant to help students test basic drive functionality.

    By the end of completing this file the student's robot should
    have both motors spinning forward and the encoders counting up.
"""

# Wait until user command before running
while not robot.buttons.isGP20Pressed():
    time.sleep(.01)
    print("Waiting for button signal")


print("Button input found; Program starting")

# Set motors to hold when set to 0 effort
robot.drivetrain.setBrakeType(robot.COAST_MODE)

# Drive forward 6 cm
robot.drivetrain.goStraight(25, 1)

time.sleep(1)

# turn 90 degrees
robot.drivetrain.goTurn(90)

time.sleep(2)

robot.drivetrain.goTurn(90, -.5)

time.sleep(1)

robot.drivetrain.goStraight(-6)

