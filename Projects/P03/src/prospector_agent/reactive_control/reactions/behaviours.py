# TODO: Add imports

import sys
sys.path.append('../lib/ecr')
sys.path.append('../lib/psa')


# This is the class "Recolher" from the UML
class Behaviours(Hierarchy):

    def __init__(self):
        super(Behaviours, self).__init__([
            Approach(),
            Avoid(),
            Bypass(),
            Roam()
        ])
