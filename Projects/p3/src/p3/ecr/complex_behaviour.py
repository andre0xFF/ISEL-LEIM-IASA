from .behaviour import Behaviour


class ComplexBehaviour(Behaviour):

    def __init__(self, behaviours):
        self._behaviours = behaviours

    def activate(self, perception):
        responses = []

        for behaviour in self._behaviours:
            response = behaviour.activate(perception)

            if response:
                responses.append(response)

        if responses:
            return self.select_response(responses)

    def select_response(self, responses):
        raise NotImplementedError("Abstract Method")
