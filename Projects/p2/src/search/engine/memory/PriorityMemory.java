package search.engine.memory;

import search.engine.tree.Node;

import java.util.Comparator;
import java.util.PriorityQueue;

public class PriorityMemory extends SearchMemory {

    public PriorityMemory(Comparator<Node> node) {
        super(new PriorityQueue<Node>(1, node));
    }
}
