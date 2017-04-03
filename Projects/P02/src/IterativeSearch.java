public class IterativeSearch extends DepthFirstSearch {

    private int depth_increment = 1;

    public int get_depth_increment() {
        return this.depth_increment;
    }

    public void set_depth_increment(int depth_increment) {
        this.depth_increment = depth_increment;
    }

    private Solution solve(Problem problem, int max_depth, int depth_increment) {

    }

    public Solution solve(Problem problem, int max_depth) {
        return this.solve(problem, max_depth, this.depth_increment);
    }
}
