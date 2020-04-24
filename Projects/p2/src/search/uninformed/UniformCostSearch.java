package search.uninformed;

import search.engine.tree.Node;
import search.informed.BestFirstSearch;
import search.problem.Problem;
import search.engine.Search;

public class UniformCostSearch extends BestFirstSearch<Problem> implements Search {

    @Override
    protected double f(Node node) {
        return node.get_cost();
    }

    @Override
    public String toString() {
        return "Uniform Cost Search";
    }
}
