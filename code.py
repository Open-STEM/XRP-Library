from WPILib import *

sonar = GroveUltrasonicRanger.GroveUltrasonicRanger(board.GP28)

#square function
def square(sidelength):
    for sides in range(4):
        driveBase.straight(sidelength)
        driveBase.turn(90)

#polygon function
def polygon(sides):
    for s in range(sides):
        driveBase.straight(150)
        driveBase.turn(360/sides)

def standoff():
    Kp = 0.2
    while True:
        distance = sonar.distance
        error = distance - 10.0
        driveBase.setEfforts(error * Kp)
        time.sleep(0.01)

def driveTillClose():
    while True:
        if sonar.distance > 10:
            driveBase.setEffort(0.60, 0.60)
        else:
            driveBase.setEffort(0, 0)
        time.sleep(0.01)

# Example using encoders of driving for a distance

# Example of turning using encoders

driveBase = drv.drive()
standoff()
