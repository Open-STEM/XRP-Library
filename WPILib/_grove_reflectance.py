from . import _grove_ultrasonic
from . import _abstract_reflectance

class GroveReflectance(_abstract_reflectance.AbstractReflectance):

    """
    Supports the old reflectance sensor. A wrapper for the GroveUltrasonic class, because
    for some reason the implementation for the reflectance sensor is identical to GroveUltrasonic
    """

    def __init__(self, leftPin, rightPin):
        print("init")
        self._leftReflectance = _grove_ultrasonic.GroveUltrasonicRanger(leftPin)
        self._rightReflectance = _grove_ultrasonic.GroveUltrasonicRanger(rightPin)
    
    # Implements AbstractReflectance
    def get_left_reflectance(self) -> float:
        """
        Gets the the reflectance of the left reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        return self._leftReflectance.get_distance()
    
    # Implements AbstractReflectance
    def get_right_reflectance(self) -> float:
        """
        Gets the the reflectance of the right reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        return self._rightReflectance.get_distance()