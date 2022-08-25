from grove_ultrasonic import GroveUltrasonicRanger as Ultrasonic

class Reflectance:
    def __init__(self, leftPin, rightPin):
        self._leftReflectance = Ultrasonic(leftPin)
        self._rightReflectance = Ultrasonic(rightPin)
    
    def getLeftReflectance(self):
        return self._leftReflectance.distance
    
    def getRightReflectance(self):
        return self._rightReflectance.distance
