# TODO: imports

import sys
sys.path.append('../lib/ecr')
# sys.path.append('../lib/psa')


class Approach(Priority):

    def __init__(self):
        super(Approach, self).__init__([
            ApproachDirection(FRT),
            ApproachDirection(ESQ),
            ApproachDirection(DIR),
        ])
