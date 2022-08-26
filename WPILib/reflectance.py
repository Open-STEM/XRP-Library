import grove_ultrasonic

class Reflectance:
    def __init__(self, leftPin, rightPin):
        self._leftReflectance = grove_ultrasonic.GroveUltrasonicRanger(leftPin)
        self._rightReflectance = grove_ultrasonic.GroveUltrasonicRanger(rightPin)
    
    def getLeftReflectance(self):
        return self._leftReflectance.distance
    
    def getRightReflectance(self):
        return self._rightReflectance.distance
