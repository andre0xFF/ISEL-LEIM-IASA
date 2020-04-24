package search.informed;

import search.problem.HeuristicProblem;
import search.problem.Solution;

public interface HeuristicSearch {

    public Solution solve(HeuristicProblem problem);
    public Solution solve(HeuristicProblem problem, int max_depth);
}
