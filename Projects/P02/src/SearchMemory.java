import java.util.ArrayList;
import java.util.Queue;

public class SearchMemory {

    protected Queue<Node> frontier;
//    protected ArrayList<Node> explored;

    public SearchMemory(Queue<Node> frontier) {
        this.frontier = frontier;
    }

    public void clean() {
        this.frontier.clear();
    }

    public void insert(Node node) {
        this.frontier.add(node);
    }

    public Node remove() {
        return this.frontier.remove();
    }

    public boolean is_empty() {
        return this.frontier.isEmpty();
    }
}
