from . import _adafruit_hcsr04
from . import _grove_ultrasonic
import board

class Ultrasonic:
    """
    A wrapper for an object that stores either the legacy or new implementation of the ultrasonic sensor
    User can set one of two modes, and get the value of either ultrasonic sensor
    """

    def __init__(self):

        # Default to new sensor
        self._sonarObject = None
        self._isLegacyMode = False

    def set_legacy_mode(self, is_legacy: bool = True) -> None:
        """
        Set whether the reflectance sensor is the old or the new analog one
        :param is_legacy: True if using the old version, False if using the new one
        :type is_legacy: bool
        """
        self._isLegacyMode = is_legacy


    def _possibly_instantiate_object(self):
        # If self._reflectanceObject is not defined, define it

        if self._sonarObject is not None:
            return

        if self._isLegacyMode:
            self._sonarObject = _grove_ultrasonic.GroveUltrasonic(board.GP28)
        else:
            self._sonarObject = _adafruit_hcsr04.AdafruitUltrasonic(board.GP7, board.GP28)
        
    
    def get_distance(self) -> float:
        """
		Return the distance measured by the sensor in cm.
        If the distance is too far, it returns a maximum value of 65535.

		:return: Distance in centimeters
		:rtype: float
		"""
        self._possibly_instantiate_object()
        return self._sonarObject.get_distance()
