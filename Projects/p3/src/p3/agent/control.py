from psa.accao import Mover as Move

class Control(object):

    def process(self, perception) -> Move:
        raise NotImplementedError("Abstract method")
