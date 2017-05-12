package search_strategies.problem;

import search_strategies.engine.tree.Operator;
import search_strategies.engine.tree.State;

public abstract class HeuristicProblem extends Problem {

    public HeuristicProblem(State state, Operator[] operator) {
        super(state, operator);
    }

    public abstract double heuristic(State state);
}
