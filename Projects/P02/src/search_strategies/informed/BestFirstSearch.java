package search_strategies.informed;

import search_strategies.engine.tree.Node;
import search_strategies.engine.SearchMechanism;
import search_strategies.engine.memory.PriorityMemory;
import search_strategies.engine.memory.SearchMemory;
import search_strategies.problem.Problem;

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