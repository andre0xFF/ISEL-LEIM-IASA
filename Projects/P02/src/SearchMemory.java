import java.util.HashMap;
import java.util.Queue;

public class SearchMemory {

    protected Queue<Node> frontier;
    protected HashMap<State, Node> explored = new HashMap<>();

    public SearchMemory(Queue<Node> frontier) {
        this.frontier = frontier;
    }

    public void clean() {
        this.frontier.clear();
        this.explored.clear();
    }

    public void insert(Node node) {
        Node explored_node = this.explored.get(node);

        if (explored_node == null ? true : explored_node.get_cost() > node.get_cost()) {
            this.explored.put(node.get_state(), node);
            this.frontier.add(node);
        }
    }

    public Node remove() {
        return this.frontier.remove();
    }

    public boolean is_empty() {
        return this.frontier.isEmpty();
    }
}
