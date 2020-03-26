package search_strategies.uninformed;

import search_strategies.engine.SearchMechanism;
import search_strategies.engine.memory.FIFOMemory;
import search_strategies.engine.memory.SearchMemory;
import search_strategies.problem.Problem;
import search_strategies.engine.Search;

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
