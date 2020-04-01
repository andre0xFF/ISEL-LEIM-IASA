from .complex_behaviour import ComplexBehaviour


class Hierarchy(ComplexBehaviour):

    def select_response(self, responses):
        if responses:
            return responses[0]
