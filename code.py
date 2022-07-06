from WPILib import *

# Drive Base
driveBase = drv.drive()

for side in range(4):
    driveBase.straight(100)
    driveBase.turn(90)
