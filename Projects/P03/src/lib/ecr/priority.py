from lib.ecr.complex_behaviour import ComplexBehaviour


class Priority(ComplexBehaviour):

    def select_response(self, responses):
        if responses:
            max(responses, key=lambda response: response.priority)
