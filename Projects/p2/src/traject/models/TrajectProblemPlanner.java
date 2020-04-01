package traject.models;

import search.problem.Problem;
import search.engine.tree.State;

public class TrajectProblemPlanner extends Problem {

    private StateLocation final_state;

    public TrajectProblemPlanner(String initial_location, String final_location, ConnectionOperator[] operators) {
        super(new StateLocation(initial_location), operators);
        this.final_state = new StateLocation(final_location);
    }

    @Override
    public boolean objective(State state) {
        return (this.final_state.equals(state));
    }
}
