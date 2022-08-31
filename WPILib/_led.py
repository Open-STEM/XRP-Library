import neopixel

class RGBLED:

    def __init__(self, pin):
        self._pixels = neopixel.NeoPixel(pin, 2)
        self._pixels.fill(0xFFFFFF)
        self._pixels.brightness = 0

    def set_color(self, red: int, green: int, blue: int):
        """
        Sets the color of the led by taking in the RGB representation of the color

        :param red: The red value (0-255)
        :type red: int
        :param green: The green value (0-255)
        :type green: int
        :param blue: The blue value (0-255)
        :type blue: int
        """
        new_color = red*16**4+green*16**2+blue
        self._pixels.fill(new_color)
    
    def set_brightness(self, brightness: float):
        """
        Sets the brightness of the two LEDs on the board

        :param brightness: The brightness to set the LEDs to [Bound from 0 (off) to 1 (max)]
        :type brightness: float
        """
        brightness = min(1,max(0,brightness))
        self._pixels.brightness = brightness

        
    
        