import time
import WPILib as robot

"""
    File meant to help students test basic drive functionality.

    By the end of completing this file the student's robot should
    have both motors spinning forward and the encoders counting up.
"""

# Wait until user command before running
while robot.buttons.isGP20Pressed():
    print("Waiting for button signal")

print("Button input found; Program starting")

# Set motors to hold when set to 0 effort
robot.drivetrain.setBrakeType(robot.BrakeType.BRAKE)

# Drive forward 6 inches
robot.drivetrain.goStraight(6, .5)

time.sleep(1)

# turn 90 degrees
robot.drivetrain.goTurn(90)

time.sleep(2)

robot.drivetrain.goTurn(90, -.5)

time.sleep(1)

robot.drivetrain.goStraight(-6)

