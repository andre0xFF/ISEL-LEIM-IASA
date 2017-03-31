public class Node {

    private int depth = 0;
    private double cost = 0;
    private Operator operator;
    private Node ancestor;
    private State state;

    public int get_depth() {
        return this.depth;
    }

    public double get_cost() {
        return this.cost;
    }

    public State get_state() {
        return this.state;
    }

    public Node get_ancestor() {
        return this.ancestor;
    }

    public void set_cost() {
        this.cost = cost;
    }

    public void set_dept(int depth) {
        this.depth = depth;
    }

    public Node(State state, Operator operator, Node ancestor) {
        this.state = state;
        this.operator = operator;
        this.ancestor = ancestor;
        this.depth = this.ancestor.get_depth() + 1;
        this.cost = operator.cost(this.ancestor.get_state(), this.get_state());
    }

    public Node(State state) {
        this.state = state;
    }
}
