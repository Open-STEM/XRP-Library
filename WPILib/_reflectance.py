from . import _grove_ultrasonic

class Reflectance:
    def __init__(self, leftPin, rightPin):
        self._leftReflectance = _grove_ultrasonic.GroveUltrasonicRanger(leftPin)
        self._rightReflectance = _grove_ultrasonic.GroveUltrasonicRanger(rightPin)
    
    def get_left_reflectance(self):
        """
        Retrieves the reflectance value from the left line follower
        :return: The reflectance value
        :rtype: float
        """
        return self._leftReflectance.get_distance()
    
    def get_right_reflectance(self):
        """
        Retrieves the reflectance value from the right line follower
        :return: The reflectance value
        :rtype: float
        """
        return self._rightReflectance.get_distance()
