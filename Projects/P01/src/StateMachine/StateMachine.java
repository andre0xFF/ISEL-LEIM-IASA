package StateMachine;

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
