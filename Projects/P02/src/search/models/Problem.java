package search.models;

public abstract class Problem {

    private State initial_state;
    private Operator[] operators;

    public State get_initial_state() {
        return this.initial_state;
    }

    public Operator[] get_operators() {
        return this.operators;
    }

    public Problem(State initial_state, Operator[] operators) {
        this.initial_state = initial_state;
        this.operators = operators;
    }

    public abstract boolean objective(State state);
}
