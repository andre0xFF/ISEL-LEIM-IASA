package search_strategies.uninformed;

import search_strategies.engine.tree.Node;
import search_strategies.informed.BestFirstSearch;
import search_strategies.problem.Problem;
import search_strategies.engine.Search;

public class UniformCostSearch extends BestFirstSearch<Problem> implements Search {

    @Override
    protected double f(Node node) {
        return node.get_cost();
    }

    @Override
    public String get_title() {
        return "Uniform Cost Search";
    }
}
