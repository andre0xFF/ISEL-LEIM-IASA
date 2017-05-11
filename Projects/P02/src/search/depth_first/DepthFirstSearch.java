package search.depth_first;

import search.engine.SearchMechanism;
import search.engine.memory.LIFOMemory;
import search.engine.memory.SearchMemory;
import search.models.Search;

public class DepthFirstSearch extends SearchMechanism implements Search {

    @Override
    protected SearchMemory start_memory() {
        return new LIFOMemory();
    }

    @Override
    public String get_title() {
        return "Depth First Search";
    }
}

