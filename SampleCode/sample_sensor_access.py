from WPILib.WPILib import *

# Polling data from the ultrasonic sensor
def ultrasonic_test():
    while True:
        try:
            print((sonar.getDistance()))
        except RuntimeError:
            print("Retrying!")
            pass
        time.sleep(0.1)

# Approaches a wall at a set speed and then stops
def drive_till_close(target_distance: float = 10.0):
    speed = 0.6
    while sonar.get_distance() > target_distance:
        drivetrain.set_effort(speed, speed)
        time.sleep(0.01)
    drivetrain.set_effort(0, 0)

# Maintains a certain distance from the wall
def standoff(target_distance: float = 10.0):
    KP = 0.2
    while True:
        distance = sonar.get_distance()
        error = distance - target_distance
        drivetrain.set_effort(error * KP, error*KP)
        time.sleep(0.01)

# Follows a line using the line followers
def line_track():
    base_effort = 0.6
    KP = 0.02
    while True:
        error = reflectance.get_left_reflectance() - reflectance.get_right_reflectance()
        drivetrain.set_effort(base_effort + error * KP, base_effort -  error * KP)

# Does nothing until a button input is found
def wait_for_button():
    print("Waiting for button signal from GP20")

    # Wait until user command before running
    while not buttons.isGP20Pressed():
        time.sleep(.01)

    print("Button input found; Program starting")