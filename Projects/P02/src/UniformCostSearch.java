public class UniformCostSearch extends BetterFirstSearch implements Search {

    @Override
    protected double f(Node node) {
        return node.get_cost();
    }
}
