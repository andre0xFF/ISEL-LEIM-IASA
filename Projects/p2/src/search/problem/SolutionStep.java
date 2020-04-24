package search.problem;

import search.engine.tree.Operator;
import search.engine.tree.State;

public interface SolutionStep {

    public State get_state();
    public Operator get_operator();
    public double get_cost();
}
