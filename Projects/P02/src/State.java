public abstract class State {

    public abstract int hashCode();

    public boolean equals(Object object) {
        return (
                object instanceof State &&
                ((State) object).hashCode() == this.hashCode()
        );
    }

}
