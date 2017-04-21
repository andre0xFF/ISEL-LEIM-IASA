import java.util.HashMap;
import java.util.Queue;

public class SearchMemory {

    protected Queue<Node> frontier;
    protected HashMap<State, Node> explored = new HashMap<>();
    private int count_nodes_frontier = 0;

    public SearchMemory(Queue<Node> frontier) {
        this.frontier = frontier;
    }

    public void clean() {
        this.frontier.clear();
        this.explored.clear();
    }

    public void insert(Node node) {
        State state = node.get_state();
        Node explored_node = this.explored.get(state);

        if (explored_node == null ? true : explored_node.get_cost() > node.get_cost()) {
            this.explored.put(node.get_state(), node);
            this.frontier.add(node);

            if (this.frontier.size() > this.count_nodes_frontier) {
                this.count_nodes_frontier = this.frontier.size();
            }
        }
    }

    public Node remove() {
        return this.frontier.remove();
    }

    public boolean is_empty() {
        return this.frontier.isEmpty();
    }
}
