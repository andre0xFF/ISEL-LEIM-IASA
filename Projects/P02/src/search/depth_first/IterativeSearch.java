package search.depth_first;

import search.models.Problem;
import search.models.Search;
import search.models.Solution;

public class IterativeSearch extends DepthFirstSearch implements Search {

    private int depth_increment = 1;

    public int get_depth_increment() {
        return this.depth_increment;
    }

    public void set_depth_increment(int depth_increment) {
        this.depth_increment = depth_increment;
    }

    private Solution solve(Problem problem, int max_depth, int depth_increment) {
        for (int i = depth_increment; i < max_depth || max_depth == -1; i += depth_increment) {
            Solution s = super.solve(problem, i);

            if (s != null) {
                return s;
            }
        }

        return null;
    }

    public Solution solve(Problem problem, int max_depth) {
        return this.solve(problem, max_depth, this.depth_increment);
    }

    @Override
    public String get_title() {
        return "Iterative Search";
    }
}