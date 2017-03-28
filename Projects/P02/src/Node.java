public class Node {

    private int depth = 0;
    private double cost;
    private Operator operator;
    private Node ancestor;
    private State state;

    public int get_depth() {
        return this.depth;
    }

    public void set_dept(int depth) {
        this.depth = depth;
    }

    public double get_cost() {
        return this.cost;
    }

    public void set_cost() {
        this.cost = cost;
    }

    public State get_state() {
        return this.state;
    }

    public Node(State state) {
        this.state = state;
    }

    public Node get_ancestor() {
        return this.ancestor;
    }

    public Node(State state, Operator operator, Node ancestor) {
        this.state = state;
        this.operator = operator;
        this.ancestor = ancestor;
    }
}
