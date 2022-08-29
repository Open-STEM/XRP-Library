from SampleCode.sample_drive_methods import *

def waitForButton():
    print("Waiting for button signal from GP20")

    # Wait until user command before running
    while not buttons.isGP20Pressed():
        time.sleep(.01)

    print("Button input found; Program starting")

def main():
    # Your code here!
    waitForButton()

    lineTrack()

    pass

main()
