package search.uninformed;

import search.engine.SearchMechanism;
import search.engine.memory.FIFOMemory;
import search.engine.memory.SearchMemory;
import search.problem.Problem;
import search.engine.Search;

public class BreadthFirstSearch extends SearchMechanism<Problem> implements Search {

    @Override
    protected SearchMemory start_memory() {
        return new FIFOMemory();
    }

    @Override
    public String toString() {
        return "Breadth First Search";
    }
}
