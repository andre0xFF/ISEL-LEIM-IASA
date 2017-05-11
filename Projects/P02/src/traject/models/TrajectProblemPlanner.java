package traject.models;

import search.models.Problem;
import search.models.State;
import traject.models.ConnectionOperator;

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
