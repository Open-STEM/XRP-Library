import time
import board
import pwmio
import rotaryio
from adafruit_motor import motor
import Encoder as enc


# Motor 1 is Right

# Motor 1
PWM_M1A = board.GP8
PWM_M1B = board.GP9

# Motor 2 is Left
PWM_M2A = board.GP10
PWM_M2B = board.GP11

# DC motor setup
M1A = pwmio.PWMOut(PWM_M1A, frequency=10000)
M1B = pwmio.PWMOut(PWM_M1B, frequency=10000)
M2A = pwmio.PWMOut(PWM_M2A, frequency=10000)
M2B = pwmio.PWMOut(PWM_M2B, frequency=10000)

motor1 = motor.DCMotor(M1A, M1B)
motor2 = motor.DCMotor(M2A, M2B)

enc1 = enc.Encoder(a=board.GP26, b=board.GP27, ticks=144)
enc2 = enc.Encoder(a=board.GP16, b=board.GP17, ticks=144)

motor1.throttle = 1
motor2.throttle = 1

while enc2.getPos() < 10000:
    time.sleep(.01)
    print(enc2.getPos())

print("reset encoder")
enc2.setPos()

while enc2.getPos() < 10000:
    time.sleep(.01)
    print(enc2.getPos())
