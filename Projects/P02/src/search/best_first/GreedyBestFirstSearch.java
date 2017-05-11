package search.best_first;

import search.engine.Node;
import search.models.HeuristicProblem;

public class GreedyBestFirstSearch extends BestFirstSearch<HeuristicProblem> {

    @Override
    protected double f(Node node) {
        return super.problem.heuristic(node.get_state());
    }

    @Override
    public String get_title() {
        return "Greedy Best First Search";
    }
}
