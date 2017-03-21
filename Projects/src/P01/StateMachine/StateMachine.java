package P01.StateMachine;

import java.util.HashMap;
import java.util.Map;

public class StateMachine<T> {

    private State<T> state;

    public StateMachine(State<T> state) {
        this.state = state;
    }

    public State<T> get_state() {
        return this.state;
    }

    public void process(T event) {
        State<T> next_state = this.state.process(event);

        if (next_state != null) {
            this.state = next_state;
        }
    }
}

class State<T> {

    private String name;
    private Map<T, State> transitions;

    public State(String name) {
        this.name = name;
        this.transitions = new HashMap<>();
    }

    public String get_name() {
        return this.name;
    }

    public void add_transition(T event, State<T> state) {
        this.transitions.put(event, state);
    }

    public State<T> process(T event) {
        return this.transitions.get(event);
    }
}
