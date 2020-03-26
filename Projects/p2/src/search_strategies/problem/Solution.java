package search_strategies.problem;

import java.util.Iterator;

public interface Solution extends Iterable<SolutionStep> {

    public Iterator<SolutionStep> iterator();
    public int get_dimension();
    public double get_cost();
}
