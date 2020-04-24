package search.uninformed;

import search.engine.SearchMechanism;
import search.problem.Problem;
import search.engine.Search;
import search.problem.Solution;

public class IterativeSearch extends DepthFirstSearch implements Search {

    private int increment = 1;

    public int get_increment() {
        return this.increment;
    }

    public void set_increment(int increment) {
        this.increment = increment;
    }

    private Solution solve(Problem problem, int max_depth, int increment) {
        for (int i = increment; i <= max_depth || max_depth == SearchMechanism.INFINITE_DEPTH; i += increment) {
            Solution s = super.solve(problem, i);

            if (s != null) {
                return s;
            }
        }

        return null;
    }

    public Solution solve(Problem problem, int max_depth) {
        return this.solve(problem, max_depth, this.increment);
    }

    @Override
    public String toString() {
        return "Iterative Search";
    }
}
