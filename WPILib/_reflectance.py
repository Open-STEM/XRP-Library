from analogio import AnalogIn

class Reflectance:
    def __init__(self, leftPin, rightPin):
        self._leftReflectance = AnalogIn(leftPin)
        self._rightReflectance = AnalogIn(rightPin)

    def _get_value(self, sensor: AnalogIn):
        MAX_ANALOG_VALUE: int = 65535
        return sensor.value / MAX_ANALOG_VALUE
    
    def get_left_reflectance(self):
        return self._get_value(self._leftReflectance)
    
    def get_right_reflectance(self):
        return self._get_value(self._rightReflectance)
