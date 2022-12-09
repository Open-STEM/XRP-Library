from . import _grove_ultrasonic

class GroveReflectance():

    """
    Supports the old reflectance sensor. A wrapper for the GroveUltrasonic class, because
    for some reason the implementation for the reflectance sensor is identical to GroveUltrasonic
    """

    def __init__(self, leftPin, rightPin):
        self._leftReflectance = _grove_ultrasonic.GroveUltrasonic(leftPin, timeout = 1)
        self._rightReflectance = _grove_ultrasonic.GroveUltrasonic(rightPin, timeout = 1)
    
    # Implements AbstractReflectance
    def get_left(self) -> float:
        """
        Gets the the reflectance of the left reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        return self._leftReflectance.get_distance()
    
    # Implements AbstractReflectance
    def get_right(self) -> float:
        """
        Gets the the reflectance of the right reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        return self._rightReflectance.get_distance()
