package search.models;

public interface Search {

    public Solution solve(Problem problem);
    public Solution solve(Problem problem, int max_depth);
}
