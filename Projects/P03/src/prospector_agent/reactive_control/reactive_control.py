from reactions.recall.recall import Recall

class ReactiveControl():

    def __init__(self, behaviour):
        self.behaviour = behaviour

    def process(self, perception):
        response = self.behaviour.activate(perception)
        return response.action
