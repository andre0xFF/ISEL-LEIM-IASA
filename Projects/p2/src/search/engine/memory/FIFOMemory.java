package search.engine.memory;

import search.engine.tree.Node;

import java.util.LinkedList;

public class FIFOMemory extends SearchMemory {

    public FIFOMemory() {
        super(new LinkedList<Node>());
    }
}
