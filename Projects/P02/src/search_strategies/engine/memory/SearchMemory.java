package search_strategies.engine.memory;

import search_strategies.engine.tree.Node;
import search_strategies.engine.tree.State;

import java.util.HashMap;
import java.util.Queue;

public class SearchMemory {

    protected Queue<Node> frontier;
    protected HashMap<State, Node> explored = new HashMap<>();
    private int frontier_nodes = 0;
    private int expanded_nodes = 0;

    public SearchMemory(Queue<Node> frontier) {
        this.frontier = frontier;
    }

    public int get_max_frontier_nodes() {
        return this.frontier_nodes;
    }

    public int get_max_expanded_nodes() {
        return this.expanded_nodes;
    }

    public void clean() {
        this.frontier.clear();
        this.explored.clear();
        this.expanded_nodes = 0;
        this.frontier_nodes = 0;
    }

    public void insert(Node node) {
        State state = node.get_state();
        Node explored_node = this.explored.get(state);

        if (explored_node == null ? true : explored_node.get_cost() > node.get_cost()) {
            this.explored.put(node.get_state(), node);
            this.frontier.add(node);
            // TODO
            if (this.frontier.size() > this.frontier_nodes) {
                this.frontier_nodes = this.frontier.size();
            }

            this.expanded_nodes++;
        }
    }

    public Node remove() {
        return this.frontier.remove();
    }

    public boolean is_empty() {
        return this.frontier.isEmpty();
    }
}
