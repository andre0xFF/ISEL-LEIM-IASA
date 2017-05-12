package search_strategies.engine;

import search_strategies.problem.Problem;
import search_strategies.problem.Solution;

public interface Search {

    public Solution solve(Problem problem);
    public Solution solve(Problem problem, int max_depth);
}
