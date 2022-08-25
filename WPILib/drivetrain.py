# Write your code here :-)
import math
import time

class Drivetrain():

    def __init__(self, leftEncodedMotor, rightEncodedMotor, wheelDiameter, wheelSpacing):

        self.leftMotor = leftEncodedMotor
        self.rightMotor = rightEncodedMotor
        
        self.wDiam = wheelDiameter
        self.wSpacing = wheelSpacing

    def straight(self, distance, lowEffort = .4, highEffort = .8):

        rotationsToDo = distance / (self.wDiam * math.pi)

        while abs(self.mL.getPos() + self.mR.getPos()) < abs(rotationsToDo * 2):
            leftDiff = abs(self.mL.getPos() - rotationsToDo)
            rightDiff = abs(self.mR.getPos() - rotationsToDo)

            if leftDiff < rightDiff:
                self.setEffort(lowEffort, highEffort, distance >= 0)
            else:
                self.setEffort(highEffort, lowEffort, distance >= 0)

        self.setEffort()
        self.setPos()

    def turn(self, degrees, lowEffort = .4, highEffort = .8):
        rotationsToDo = (degrees/360) * (math.pi * self.wSpacing) / (self.wDiam * math.pi)

        ## Turning Direction
        ##      Negative Left
        ##      Positive Right

        #print("Turning")
        #print("rotationsToDo " + str(rotationsToDo))

        while abs(self.mR.getPos() - self.mL.getPos()) < abs(rotationsToDo * 2):
            leftDiff  = abs(rotationsToDo) - abs(self.mL.getPos())
            rightDiff = abs(rotationsToDo) - abs(self.mR.getPos())

            if leftDiff < rightDiff:
                self.setEffort(lowEffort, -highEffort, degrees <= 0)
            else:
                self.setEffort(highEffort, -lowEffort, degrees <= 0)

        self.setEffort()
        self.setPos()

    def arcTurn(self, degrees, speed, radius):
        pass

    def setEffort(self, leftEffort = 0, rightEffort = 0, doNotFlip = True):
        if doNotFlip:
            self.mL.setEffort(leftEffort)
            self.mR.setEffort(rightEffort)
        else:
            self.mL.setEffort(-leftEffort)
            self.mR.setEffort(-rightEffort)

    def setEfforts(self, effort = 0, doNotFlip = True):
        self.setEffort(effort, effort, doNotFlip)

    def setPos(self, left=0, right=0):
        self.mL.setPos(left)
        self.mR.setPos(right)




