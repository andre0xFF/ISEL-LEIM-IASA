public interface SolutionStep {

    public State get_state();
    public Operator get_operator();
    public double get_cost();
}
