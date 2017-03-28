import java.util.Iterator;
import java.util.LinkedList;

public class Path implements Solution {

    private int dimension;
    private double cost;
    private LinkedList list;

    public int get_dimension() {
        return this.dimension;
    }

    public double get_cost() {
        return this.cost;
    }

    public Iterator<SolutionStep> iterator() {
        return this.list.iterator();
    }

    public void join_start(Node node) {
        this.list.addFirst(node);
    }
}
