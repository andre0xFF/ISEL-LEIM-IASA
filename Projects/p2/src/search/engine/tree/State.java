package search.engine.tree;

public abstract class State {

    public abstract int hashCode();

    public boolean equals(Object object) {
        return (
                object instanceof State &&
                object.hashCode() == this.hashCode()
        );
    }

}
