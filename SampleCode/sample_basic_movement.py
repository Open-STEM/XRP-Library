import time
import WPILib.WPILib as robot

"""
    File meant to help students test basic drive functionality.

    By the end of completing this file the student's robot should
    have the robot driving straight and turning after waiting for a button press.
"""


print("Waiting for button signal from GP20")

# Wait until user command before running
while not robot.buttons.isGP20Pressed():
    time.sleep(.01)

print("Button input found; Program starting")

# Drive forward cm
robot.drivetrain.goStraight(25, 0.5)

time.sleep(1)

# turn 90 degrees clockwise
robot.drivetrain.goTurn(90,0.5)

time.sleep(1)

# turn 90 degrees counter clockwise by setting speed negative
robot.drivetrain.goTurn(90, -0.5)

time.sleep(1)

# drive backwards 25 cm by setting distance negative. s
# There is no difference between setting speed or distance negative, both work
robot.drivetrain.goStraight(-25,0.5)

