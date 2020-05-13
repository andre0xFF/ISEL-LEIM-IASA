package machine.intelligence;

import game.environment.Stimulus;

public class HierarchicalBehavior implements Behavior {

    private Behavior[] behaviors;

    public HierarchicalBehavior(Behavior[] behaviors) {
        this.behaviors = behaviors;
    }

    public Action activate(Stimulus stimulus) {
        for (Behavior behavior : this.behaviors) {
            Action action = behavior.activate(stimulus);

            if (action != null) {
                return action;
            }
        }

        return null;
    }
}
