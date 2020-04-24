package Game.AI;

import Game.Environment.Stimulus;

public interface Behavior {

    public Action activate(Stimulus stimulus);
}
