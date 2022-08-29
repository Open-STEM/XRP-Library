from WPILib.WPILib import *

# Polling data from the ultrasonic sensor
def ultrasonicTest():
    while True:
        try:
            print((sonar.getDistance()))
        except RuntimeError:
            print("Retrying!")
            pass
        time.sleep(0.1)

# Follows a line using the line followers
def lineTrack():
    baseEffort = 0.6
    KP = 0.02
    while True:
        error = reflectance.getLeftReflectance() - reflectance.getRightReflectance()
        drivetrain.setEffort(baseEffort + error * KP, baseEffort -  error * KP)