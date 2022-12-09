from analogio import AnalogIn

class AnalogReflectance:

    """
    Implements for the new reflectance sensor.
    Reads from analog in and converts to a float from 0 (white) to 1 (black)
    """

    def __init__(self, leftPin, rightPin):
        self._leftReflectance = AnalogIn(leftPin)
        self._rightReflectance = AnalogIn(rightPin)

    def _get_value(self, sensor: AnalogIn) -> float:
        MAX_ANALOG_VALUE: int = 65535
        return sensor.value / MAX_ANALOG_VALUE
    
    # Implements AbstractReflectance
    def get_left(self) -> float:
        """
        Gets the the reflectance of the left reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        return self._get_value(self._leftReflectance)
    
    # Implements AbstractReflectance
    def get_right(self) -> float:
        """
        Gets the the reflectance of the right reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        return self._get_value(self._rightReflectance)