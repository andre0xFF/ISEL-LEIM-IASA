package search.engine.tree;

import search.problem.Solution;
import search.problem.SolutionStep;

import java.util.Iterator;
import java.util.LinkedList;

public class Path implements Solution {

    private LinkedList<SolutionStep> list = new LinkedList();

    public int get_dimension() {
        if (this.list.isEmpty()) {
            return 0;
        }

        return this.list.size();
    }

    public double get_cost() {
        if (this.list.isEmpty()) {
            return 0;
        }

        return this.list.getLast().get_cost();
    }

    public Iterator<SolutionStep> iterator() {
        return this.list.iterator();
    }

    public void join_start(Node node) {
        this.list.addFirst(node);
    }
}