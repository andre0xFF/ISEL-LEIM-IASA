package search_strategies.engine.tree;

public interface Operator {
    public State apply(State state);
    public float get_cost(State state, State successor);
}
