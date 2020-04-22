package search.informed;

import search.engine.tree.Node;
import search.problem.HeuristicProblem;

public class AStarSearch extends BestFirstSearch<HeuristicProblem> implements HeuristicSearch {

    @Override
    protected double f(Node node) {
        return node.get_cost() + super.problem.heuristic(node.get_state());
    }

    @Override
    public String toString() {
        return "A* Search";
    }
}