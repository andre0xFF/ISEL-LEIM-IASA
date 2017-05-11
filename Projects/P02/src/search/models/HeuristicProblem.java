package search.models;

public abstract class HeuristicProblem extends Problem {

    public HeuristicProblem(State state, Operator[] operator) {
        super(state, operator);
    }

    public abstract double heuristic(State state);
}
