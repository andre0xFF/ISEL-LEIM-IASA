package search_strategies.engine.memory;

import search_strategies.engine.tree.Node;

import java.util.Collections;
import java.util.LinkedList;

public class LIFOMemory extends SearchMemory {

    public LIFOMemory() {
        super(Collections.asLifoQueue(new LinkedList<Node>()));
    }
}