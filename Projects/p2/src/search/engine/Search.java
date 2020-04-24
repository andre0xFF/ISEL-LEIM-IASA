package search.engine;

import search.problem.Problem;
import search.problem.Solution;

public interface Search {

    public Solution solve(Problem problem);
    public Solution solve(Problem problem, int max_depth);
}
