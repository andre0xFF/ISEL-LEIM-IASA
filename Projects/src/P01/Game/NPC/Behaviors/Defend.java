package P01.Game.NPC.Behaviors;

import P01.Game.AI.Behavior;
import P01.Game.AI.HierarchicalBehavior;
import P01.Game.AI.Reaction;
import P01.Game.Environment.EnvironmentAction;
import P01.Game.Environment.EnvironmentEvent;

public class Defend extends HierarchicalBehavior {

    public Defend() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.DEFEND)
        });
    }
}
