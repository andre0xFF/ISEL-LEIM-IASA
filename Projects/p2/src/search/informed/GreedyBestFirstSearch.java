package search.informed;

import search.engine.tree.Node;
import search.problem.HeuristicProblem;

public class GreedyBestFirstSearch extends BestFirstSearch<HeuristicProblem> implements HeuristicSearch {

    @Override
    protected double f(Node node) {
        return super.problem.heuristic(node.get_state());
    }

    @Override
    public String toString() {
        return "Greedy Best First Search";
    }
}
