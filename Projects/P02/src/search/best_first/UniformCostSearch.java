package search.best_first;

import search.engine.Node;
import search.models.Problem;
import search.models.Search;
import search.models.Solution;

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
