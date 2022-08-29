from WPILib import *
import GroveUltrasonicRanger


refl = GroveUltrasonicRanger.GroveUltrasonicRanger(sig_pin=board.GP26)
for refTest in range(1000):
    try:
        print((refl.distance,))
    except RuntimeError as e:
        print("Retrying due to exception =", e)
        pass

    time.sleep(0.3)
