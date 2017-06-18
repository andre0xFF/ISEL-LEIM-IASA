from lib.ecr.behaviour import Behaviour


class Reaction(Behaviour):

    def activate(self, perception):
        stimulus = self._detect_stimulus(perception)

        if stimulus is not None and stimulus is not False:
            response = self._generate_response(stimulus)
            return response

    def _generate_response(self, stimulus):
        "''"

    def _detect_stimulus(self, perception):
        "''"
