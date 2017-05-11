import sys
sys.path.append('../lib')
sys.path.append('../agent_prospector')
import psa
from prospector_agent import ProspectorAgent
from reactive_control.reactive_control import ReactiveControl
from reactive_control.reactions.recall import Recall as Behaviour

psa.start('amb/amb1.das')
psa.execute(ProspectorAgent(ReactiveControl(Behaviour())))
