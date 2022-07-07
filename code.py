# Write your code here :-)
import time
import board
import pwmio
from adafruit_motor import servo
import GroveUltrasonicRanger

sonar = GroveUltrasonicRanger.GroveUltrasonicRanger(sig_pin=board.GP28)
pwm = pwmio.PWMOut(board.GP12, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

INCREMENT = 2
DECREMENT = -2

servo_dir = INCREMENT
servo_pos = 90
prev_time = 0

my_servo.angle = servo_pos

while True:
    servo_pos = servo_pos + servo_dir
    if servo_pos == 0:
        servo_dir = INCREMENT
    elif servo_pos == 180:
        servo_dir = DECREMENT
    my_servo.angle = servo_pos

    try:
        print((sonar.distance,))
    except RuntimeError as e:
        print("Retrying due to exception =", e)
        pass
    time.sleep(0.1)
