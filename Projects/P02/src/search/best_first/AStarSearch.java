package search.best_first;

import search.best_first.BestFirstSearch;
import search.engine.Node;
import search.models.HeuristicProblem;

public class AStarSearch extends BestFirstSearch<HeuristicProblem> {

    @Override
    protected double f(Node node) {
        return node.get_cost() + super.problem.heuristic(node.get_state());
    }

    @Override
    public String get_title() {
        return "A* Search";
    }
}