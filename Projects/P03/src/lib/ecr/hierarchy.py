class Hierarchy(ComplexBehaviour):

    #  Constructor is inherited
    # def __init__(self, behaviours):
    #     super(behaviours)

    def select_response(self, responses):
        if responses:
            return responses[0]
