package search_strategies.informed;

import search_strategies.engine.tree.Node;
import search_strategies.problem.HeuristicProblem;

public class AStarSearch extends BestFirstSearch<HeuristicProblem> implements HeuristicSearch {

    @Override
    protected double f(Node node) {
        return node.get_cost() + super.problem.heuristic(node.get_state());
    }

    @Override
    public String get_title() {
        return "A* Search";
    }
}