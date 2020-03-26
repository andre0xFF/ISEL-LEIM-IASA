package search_strategies.uninformed;

import search_strategies.engine.SearchMechanism;
import search_strategies.engine.memory.LIFOMemory;
import search_strategies.engine.memory.SearchMemory;
import search_strategies.engine.Search;

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

