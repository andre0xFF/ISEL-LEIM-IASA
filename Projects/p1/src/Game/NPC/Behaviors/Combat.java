package Game.NPC.Behaviors;

import Game.AI.Behavior;
import Game.AI.HierarchicalBehavior;
import Game.AI.Reaction;
import Game.Environment.EnvironmentAction;
import Game.Environment.EnvironmentEvent;

public class Combat extends HierarchicalBehavior {

    public Combat() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.ATTACK),
                new Reaction(EnvironmentEvent.DEFEAT, EnvironmentAction.START)
        });
    }
}
