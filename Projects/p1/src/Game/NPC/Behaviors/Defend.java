package Game.NPC.Behaviors;

import Game.AI.Behavior;
import Game.AI.HierarchicalBehavior;
import Game.AI.Reaction;
import Game.Environment.EnvironmentAction;
import Game.Environment.EnvironmentEvent;

public class Defend extends HierarchicalBehavior {

    public Defend() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.DEFEND)
        });
    }
}
