package problems.path.models;

import search.engine.tree.Operator;
import search.engine.tree.State;

public class ConnectionOperator implements Operator {

    private final StateLocation origin_state;
    private final StateLocation destination_state;
    private final float connection_cost;

    public ConnectionOperator(String initial_location, String final_location, float connection_cost) {
        this.origin_state = new StateLocation(initial_location);
        this.destination_state = new StateLocation(final_location);
        this.connection_cost = connection_cost;
    }

    @Override
    public State apply(State state) {
        if (state.equals(this.origin_state)) {
            return this.destination_state;
        }

        return null;
    }

    @Override
    public float get_cost(State state, State successor) {
        return this.connection_cost;
    }
}
