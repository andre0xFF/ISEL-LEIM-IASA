package search.engine;

import search.engine.memory.SearchMemory;
import search.models.*;

public abstract class SearchMechanism <P extends Problem> {

    private SearchMemory search_memory;
    protected P problem;

    public SearchMemory get_search_memory() {
        return this.search_memory;
    }

    public SearchMechanism() {
        this.search_memory = this.start_memory();
    }

    protected abstract SearchMemory start_memory();

    public Solution solve(P problem) {
        return this.solve(problem, -1);
    }

    public Solution solve(P problem, int max_depth) {
        this.problem = problem;
        this.search_memory.clean();

        Node initial_node = new Node(this.problem.get_initial_state());
        this.search_memory.insert(initial_node);

        while (!this.search_memory.is_empty()) {
            Node node = this.search_memory.remove();

            if (this.problem.objective(node.get_state())) {
                return this.generate_solution(node);
            }
            else {
                if (node.get_depth() < max_depth || max_depth == -1) {
                    this.expand(node);
                }
            }
        }

        return null;
    }

    private void expand(Node node) {
        State state = node.get_state();
        Operator[] operators = this.problem.get_operators();

        for (Operator operator : operators) {
            State operator_state = operator.apply(state);

            if (operator_state != null) {
                Node successor_node = new Node(operator_state, operator, node);
                this.search_memory.insert(successor_node);
            }
        }

    }

    private Solution generate_solution(Node final_node) {
        Path path = new Path();

        while(final_node != null) {
           path.join_start(final_node);
           final_node = final_node.get_ancestor();
        }

        return path;
    }

    public abstract String get_title();
}