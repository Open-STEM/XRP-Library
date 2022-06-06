# Write your code here :-)
import rotaryio

class encoder():

    def __init__(self, a, b, ticks, flip=False):
        self.ticksPerRev = ticks
        self.reverse = flip
        self.encoder = rotaryio.IncrementalEncoder(a, b)
        print("initialized")

    def getPos(self, inTicks=False, roundToo=3):
        """
            inTicks     boolean     True ~ in Ticks     False ~ in Rotations
        """
        r = self.encoder.position
        if self.reverse:
            r *= -1
        if not inTicks:
            r = r / self.ticksPerRev
        return round(r, roundToo)

    def setPos(self, pos=0):
        """
            pos         float   number of rotations to set encoder to
        """
        self.encoder.position = round(pos * self.ticksPerRev)


