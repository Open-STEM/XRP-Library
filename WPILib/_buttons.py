import board
from digitalio import DigitalInOut, Direction, Pull

class Buttons:

    def _createButton(self, buttonPin):
        btn = DigitalInOut(buttonPin)
        btn.direction = Direction.INPUT
        btn.pull = Pull.UP
        return btn

    def __init__(self):
        self._buttonGP20 = self._createButton(board.GP20)
        self._buttonGP21 = self._createButton(board.GP21)

    def is_GP20_pressed(self) -> bool:
        """
        Get whether the GP20 button on the RP2040 microcontroller has been pressed
        : return: if the GP20 button was pressed
        : rtype: bool
        """
        return not self._buttonGP20.value

    def is_GP21_pressed(self) -> bool:
        """
        Get whether the GP21 button on the RP2040 microcontroller has been pressed
        : return: if the GP21 button was pressed
        : rtype: bool
        """
        return not self._buttonGP21.value
