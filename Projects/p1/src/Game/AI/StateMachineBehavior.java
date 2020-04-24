package Game.AI;

import Game.Environment.Stimulus;
import StateMachine.State;
import StateMachine.StateMachine;

import java.util.HashMap;
import java.util.Map;

public abstract class StateMachineBehavior implements Behavior {

    private StateMachine<Stimulus> machine;
    private Map<State, Behavior> behaviors = new HashMap<>();

    public StateMachineBehavior() {
        this.machine = this.start();
    }

    protected abstract StateMachine<Stimulus> start();

    public State<Stimulus> get_state() {
        return this.machine.get_state();
    }

    public void add_behavior(State<Stimulus> state, Behavior behavior) {
        this.behaviors.put(state, behavior);
    }

    public Action activate(Stimulus stimulus) {
        Behavior behavior = this.behaviors.get(this.machine.get_state());
        Action action = behavior != null ? behavior.activate(stimulus) : null;
        this.machine.process(stimulus);
        return action;
    }
}

