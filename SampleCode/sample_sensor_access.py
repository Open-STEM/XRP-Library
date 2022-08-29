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

# Follows a line using the line followers
def line_track():
    baseEffort = 0.6
    KP = 0.02
    while True:
        error = reflectance.getLeftReflectance() - reflectance.getRightReflectance()
        drivetrain.setEffort(baseEffort + error * KP, baseEffort -  error * KP)

# Does nothing until a button input is found
def wait_for_button():
    print("Waiting for button signal from GP20")

    # Wait until user command before running
    while not buttons.isGP20Pressed():
        time.sleep(.01)

    print("Button input found; Program starting")