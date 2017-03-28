package Game.NPC.Behaviors;

import Game.AI.Behavior;
import Game.AI.HierarchicalBehavior;
import Game.AI.Reaction;
import Game.Environment.EnvironmentAction;
import Game.Environment.EnvironmentEvent;

public class Inspection extends HierarchicalBehavior {

    public Inspection() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.NOISE, EnvironmentAction.SEARCH),
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.APPROACH)
        });
    }
}
