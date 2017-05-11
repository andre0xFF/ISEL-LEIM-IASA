package search.engine.memory;

import search.engine.Node;

import java.util.LinkedList;
import java.util.Queue;

public class FIFOMemory extends SearchMemory {

    public FIFOMemory() {
        super(new LinkedList<Node>());
    }
}
