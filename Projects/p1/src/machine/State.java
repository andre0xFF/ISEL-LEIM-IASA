package machine;

import java.util.HashMap;
import java.util.Map;

public class State<T> {

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
