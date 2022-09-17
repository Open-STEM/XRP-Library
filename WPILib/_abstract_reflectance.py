
class AbstractReflectance:

    """
    An interface for reading the two reflectance sensors.
    At the moment, there are the grove ultrasonic and analog implementations.
    """

    # @abstractmethod because circuitpython does not support abc
    def get_left_reflectance(self) -> float:
        """
        Gets the the reflectance of the left reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        pass

    # @abstractmethod because circuitpython does not support abc
    def get_right_reflectance(self) -> float:
        """
        Gets the the reflectance of the right reflectance sensor
        :return: The reflectance ranging from 0 (white) to 1 (black)
        :rtype: float
        """
        pass