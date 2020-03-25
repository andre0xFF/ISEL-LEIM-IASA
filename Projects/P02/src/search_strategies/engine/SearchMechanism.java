package search_strategies.engine;

import search_strategies.engine.memory.SearchMemory;
import search_strategies.engine.tree.Node;
import search_strategies.engine.tree.Operator;
import search_strategies.engine.tree.Path;
import search_strategies.engine.tree.State;
import search_strategies.problem.*;

public abstract class SearchMechanism<P extends Problem> {

    public static final int INFINITE_DEPTH = -1;
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

        return this.solve(problem, SearchMechanism.INFINITE_DEPTH);
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

            if (node.get_depth() < max_depth || max_depth == SearchMechanism.INFINITE_DEPTH) {
                this.expand(node);
            }
        }

        return null;
    }

    private void expand(Node node) {

        State state = node.get_state();
        Operator[] operators = this.problem.get_operators();

        for (Operator operator : operators) {
            State new_state = operator.apply(state);

            if (new_state != null) {
                Node successor_node = new Node(new_state, operator, node);
                this.search_memory.insert(successor_node);
            }
        }
    }

    private Solution generate_solution(Node node) {

        Path path = new Path();

        while(node != null) {
           path.join_start(node);
           node = node.get_ancestor();
        }

        return path;
    }

    public abstract String get_title();
}
