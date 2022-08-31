from WPILib.WPILib import *

"""
    By the end of this file students will learn how to use the on-board buttons and LEDS,
    as well as control a servo that may be connected.
"""

# Does nothing until any button input is found
def wait_for_button():
    print("Waiting for button signal from either button")

    # Wait until user command before running
    while not (buttons.is_GP20_pressed() or buttons.is_GP21_pressed()):
        time.sleep(.01)

    print("Button input found; Program starting")

# Cycles through the 3 primary colors (for light) with decreasing brightness
def test_leds():
    brightness = 1
    while brightness > 0:
        led.set_brightness(brightness)
        led.set_color(255,0,0)
        time.sleep(0.5)
        led.set_color(0,255,0)
        time.sleep(0.5)
        led.set_color(0,0,255)
        time.sleep(0.5)
        brightness -= 0.1
    led.set_color(0,0,0)
    led.set_brightness(0)

# Test moving to both extremes of the servo motion and some middle value
def test_servo():
    servo.setDegrees(135)
    time.sleep(2)
    servo.setDegrees(0)
    time.sleep(2)
    servo.setDegrees(60)
    time.sleep(2)