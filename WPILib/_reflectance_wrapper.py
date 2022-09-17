from . import _abstract_reflectance
from . import _analog_reflectance
from . import _grove_reflectance
from . import _analog_reflectance
from . import _abstract_reflectance
import board

class ReflectanceWrapper:

    """
    A wrapper for an object that stores either the legacy or new implementation of the reflectance sensor
    User can set one of two modes, and get the value of either reflectance sensor
    """

    def __init__(self):

        # Default to new sensor
        self.set_legacy_mode(False)

    def set_legacy_mode(self, is_legacy: bool = True) -> None:
        """
        Set whether the reflectance sensor is the old or the new analog one
        :param is_legacy: True if using the old version, False if using the new one
        :type is_legacy: bool
        """
        if is_legacy:
            self._reflectanceObject: _abstract_reflectance.AbstractReflectance = _grove_reflectance.GroveReflectance(board.GP26, board.GP27)
        else:
            self._reflectanceObject: _abstract_reflectance.AbstractReflectance = _analog_reflectance.AnalogReflectance(board.GP26, board.GP27)

    
    def get_left_reflectance(self) -> float:
        """
        Gets the the reflectance of the left reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        return self._reflectanceObject.get_left_reflectance()
    

    def get_right_reflectance(self) -> float:
        """
        Gets the the reflectance of the right reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        return self._reflectanceObject.get_right_reflectance()