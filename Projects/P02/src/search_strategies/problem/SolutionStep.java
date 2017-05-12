package search_strategies.problem;

import search_strategies.engine.tree.Operator;
import search_strategies.engine.tree.State;

public interface SolutionStep {

    public State get_state();
    public Operator get_operator();
    public double get_cost();
}
