from SampleCode.sample_drive_methods import square
from SampleCode.sample_sensor_access import line_track
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

    # Wait until user to release button before running
    while (buttons.is_GP20_pressed() or buttons.is_GP21_pressed()):
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
        brightness -= 0.25
    led.set_color(0,0,0)
    led.set_brightness(0)

# Test moving to both extremes of the servo motion and some middle value
def test_servo():
    servo.set_degrees(135)
    time.sleep(2)
    servo.set_degrees(0)
    time.sleep(2)
    servo.set_degrees(60)
    time.sleep(2)

# Installation Verification Program
def ivp():
    while not buttons.is_GP20_pressed() and not buttons.is_GP21_pressed():
        print(f"Left Reflectance: {reflectance.get_left_reflectance()}, Right Reflectance: {reflectance.get_right_reflectance()}")
        time.sleep(0.1)
    while (buttons.is_GP20_pressed() or buttons.is_GP21_pressed()):
        time.sleep(.01)
    while not buttons.is_GP20_pressed() and not buttons.is_GP21_pressed():
        print(f"Ultrasonic Distance: {sonar.get_distance()}")
        time.sleep(0.1)
    while (buttons.is_GP20_pressed() or buttons.is_GP21_pressed()):
        time.sleep(.01)
    print("Testing Servo")
    test_servo()
    print("Testing LEDs")
    wait_for_button()
    test_leds()
    print("Testing Drivetrain:")
    wait_for_button()
    square(20)