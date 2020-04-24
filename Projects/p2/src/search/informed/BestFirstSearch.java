package search.informed;

import search.engine.tree.Node;
import search.engine.SearchMechanism;
import search.engine.memory.PriorityMemory;
import search.engine.memory.SearchMemory;
import search.problem.Problem;

import java.util.Comparator;

public abstract class BestFirstSearch<P extends Problem> extends SearchMechanism<P> implements Comparator<Node> {

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