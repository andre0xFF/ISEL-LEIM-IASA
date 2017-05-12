package search_strategies.engine.memory;

import search_strategies.engine.tree.Node;

import java.util.LinkedList;

public class FIFOMemory extends SearchMemory {

    public FIFOMemory() {
        super(new LinkedList<Node>());
    }
}
