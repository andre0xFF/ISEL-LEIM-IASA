package search.breadth_first;

import search.engine.SearchMechanism;
import search.engine.memory.FIFOMemory;
import search.engine.memory.SearchMemory;
import search.models.Problem;
import search.models.Search;

public class BreadthFirstSearch extends SearchMechanism<Problem> implements Search {

    @Override
    protected SearchMemory start_memory() {
        return new FIFOMemory();
    }

    @Override
    public String get_title() {
        return "Breadth First Search";
    }
}
