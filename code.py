from WPILib.WPILib import *

## Optional imports for use with sample code
from SampleCode.sample_drive_methods import *
from SampleCode.sample_sensor_access import *
from SampleCode.sample_miscellaneous import *

def main():
    #wait_for_button()
    #
    # Your code goes here!
    #

    while True:
        print(round(reflectance.get_left_reflectance(), 2), round(reflectance.get_right_reflectance(),2))
        time.sleep(0.1)

main()
