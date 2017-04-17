public interface Operator {
    public State apply(State state);
    public Float cost(State state, State successor);
}
