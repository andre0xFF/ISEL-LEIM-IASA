from lib.ecr.behaviour import Behaviour


class Reaction(Behaviour):

    def activate(self, perception):
        stimulus = self.detect_stimulus(perception)

        if stimulus is not None and stimulus is not False:
            response = self.generate_response(stimulus)
            return response

    def generate_response(self, stimulus):
        abstract

    def detect_stimulus(self, perception):
        abstract
