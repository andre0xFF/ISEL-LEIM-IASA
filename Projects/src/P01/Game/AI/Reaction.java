package P01.Game.AI;

public class Reaction implements Behavior {

    private Stimulus stimulus;
    private Action action;

    public Reaction(Stimulus stimulus, Action action) {
        this.stimulus = stimulus;
        this.action = action;
    }

    @Override
    public Action activate(Stimulus stimulus) {
        return stimulus == this.stimulus ? this.action : null;
    }
}
