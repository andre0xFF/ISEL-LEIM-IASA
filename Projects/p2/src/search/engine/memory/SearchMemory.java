package search.engine.memory;

import search.engine.tree.Node;
import search.engine.tree.State;

import java.util.HashMap;
import java.util.Queue;

public class SearchMemory {

    protected Queue<Node> frontier;
    protected HashMap<State, Node> explored = new HashMap<>();
    private int frontier_nodes = 0;
    private int explored_nodes = 0;

    public SearchMemory(Queue<Node> frontier) {
        this.frontier = frontier;
    }

    public int get_max_frontier_nodes() {
        return this.frontier_nodes;
    }

    public int get_spacial_complexity() {
        return this.frontier_nodes;
    }

    public int get_max_expanded_nodes() {
        return this.explored_nodes;
    }

    public int get_temporal_complexity() {
        return this.explored_nodes;
    }

    public void clean() {
        this.frontier.clear();
        this.explored.clear();
    }

    public void insert(Node node) {
        // Check if the new node's state was previously explored and if the
        // previously explored node's cost is higher than new node's cost
        State state = node.get_state();
        Node explored_node = this.explored.get(state);

        if (explored_node == null || explored_node.get_cost() > node.get_cost()) {
            this.explored.put(node.get_state(), node);
            this.frontier.add(node);

            // Space complexity: The max number of nodes in the frontier
            if (this.frontier.size() > this.frontier_nodes) {
                this.frontier_nodes = this.frontier.size();
            }
        }

        // Time complexity: Total number of explored nodes
        this.explored_nodes++;
    }

    public Node remove() {
        return this.frontier.remove();
    }

    public boolean is_empty() {
        return this.frontier.isEmpty();
    }
}
