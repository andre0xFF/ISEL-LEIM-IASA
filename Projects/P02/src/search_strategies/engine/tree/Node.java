package search_strategies.engine.tree;

import search_strategies.problem.SolutionStep;

public class Node implements SolutionStep {

    private int depth = 0;
    private double cost = 0;
    private Operator operator;
    private Node ancestor;
    private State state;

    public int get_depth() {
        return this.depth;
    }

    @Override
    public double get_cost() {
        return this.cost;
    }

    @Override
    public State get_state() {
        return this.state;
    }

    @Override
    public Operator get_operator() {
        return this.operator;
    }

    public Node get_ancestor() {
        return this.ancestor;
    }

    public void set_cost() {
        this.cost = cost;
    }

    public void set_depth(int depth) {
        this.depth = depth;
    }

    public Node(State state, Operator operator, Node ancestor) {
        this(state);
        this.operator = operator;
        this.ancestor = ancestor;

        if (this.ancestor != null) {
            this.depth = this.ancestor.get_depth() + 1;
            this.cost = operator.get_cost(this.ancestor.get_state(), this.get_state());
        }
    }

    public Node(State state) {
        this.state = state;
    }
}
