from overrides import overrides

from Surprisable import Surprisable


class BasketBall(Surprisable):
    @overrides
    def activate_surprise(self):
        print("You got a surprise! Congratulations!")
