package traject.models;

import search_strategies.engine.tree.State;

public class StateLocation extends State {

    private String location;

    public StateLocation(String location) {
        this.location = location;
    }

    @Override
    public int hashCode() {
        return location.hashCode();
    }

    @Override
    public String toString() {
        return location;
    }
}
