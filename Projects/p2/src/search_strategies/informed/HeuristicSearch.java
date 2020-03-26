package search_strategies.informed;

import search_strategies.problem.HeuristicProblem;
import search_strategies.problem.Solution;

public interface HeuristicSearch {

    public Solution solve(HeuristicProblem problem);
    public Solution solve(HeuristicProblem problem, int max_depth);
}
