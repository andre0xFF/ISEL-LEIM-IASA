package P01.Game.NPC.Behaviors;

import P01.Game.AI.Behavior;
import P01.Game.AI.HierarchicalBehavior;
import P01.Game.AI.Reaction;
import P01.Game.Environment.EnvironmentAction;
import P01.Game.Environment.EnvironmentEvent;

public class Inspection extends HierarchicalBehavior {

    public Inspection() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.NOISE, EnvironmentAction.SEARCH),
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.APPROACH)
        });
    }
}
