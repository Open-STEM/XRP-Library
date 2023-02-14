from . import _analog_reflectance
from . import _grove_reflectance
import board

class Reflectance:

    """
    A wrapper for an object that stores either the legacy or new implementation of the reflectance sensor
    User can set one of two modes, and get the value of either reflectance sensor
    """

    def __init__(self):

        # Default to new sensor
        self._reflectanceObject = None
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

        if self._reflectanceObject is not None:
            return

        if self._isLegacyMode:
            self._reflectanceObject = _grove_reflectance.GroveReflectance(board.GP26, board.GP27)
        else:
            self._reflectanceObject = _analog_reflectance.AnalogReflectance(board.GP27, board.GP26)
        
    
    def get_left(self) -> float:
        """
        Gets the the reflectance of the left reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        self._possibly_instantiate_object()
        return self._reflectanceObject.get_left()
    

    def get_right(self) -> float:
        """
        Gets the the reflectance of the right reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        self._possibly_instantiate_object()
        return self._reflectanceObject.get_right()