package search.engine.memory;

import search.engine.Node;

import java.util.Collections;
import java.util.LinkedList;

public class LIFOMemory extends SearchMemory {

    public LIFOMemory() {
        super(Collections.asLifoQueue(new LinkedList<Node>()));
    }
}