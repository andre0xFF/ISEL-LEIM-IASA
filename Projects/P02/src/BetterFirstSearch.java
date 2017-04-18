import java.util.Comparator;

public abstract class BetterFirstSearch<P extends Problem> extends SearchMechanism<P> implements Comparator<Node> {

    @Override
    public int compare(Node o1, Node o2) {
        return Double.compare(f(o1), f(o2));
    }

    protected abstract double f(Node node);

    @Override
    protected SearchMemory start_memory() {
        return new PriorityMemory(this);
    }
}