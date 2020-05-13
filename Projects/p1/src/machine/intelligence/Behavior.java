package machine.intelligence;

import game.environment.Stimulus;

public interface Behavior {

    public Action activate(Stimulus stimulus);
}
