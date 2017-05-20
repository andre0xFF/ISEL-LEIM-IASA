class DeliberativeControl():

    def DeliberativeControl(self, planner):
        self._planner = planner

    def reconsider(self):
        # and -> or
        # return self._world_model.changed or self._planner.pending_plan() or not self._objectives

    def deliberate(self):
        # self._objectives = [TODOS OS ALVOS]

    def plan(self):
        pass

    def execute(self):
        pass

    def process(self, perception):
        self.take(perception)

        if self.reconsider():
            self.deliberate()
            self.plan()

        action = self.execute()
        return action

    # assimilar
    def take(self, perception):
        pass
