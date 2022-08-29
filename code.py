import SampleCode.code_drive_and_turn

#drive straight
def driveStraight():
    driveBase.straight(200)

#simeple turn
def simpleTurn():
    driveBase.setEffort(0.5, 0.8)

def pointTurn():
    driveBase.setEffort(-0.8, 0.8)

def swingTurn():
    driveBase.setEffort(0, 0.8)

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

# Driving in a circle
def circle():
    while True:
        driveBase.setEffort(0.6, 0.75)

# Example using encoders of driving for a distance

# Example of turning using encoders

def lineTrack():
    baseEffort = 0.6
    Kp = 0.02
    while True:
        error = refl.right() - refl.left()
        driveBase.setEffort(0.6 + error * Kp, 0.6 -  error * Kp)


