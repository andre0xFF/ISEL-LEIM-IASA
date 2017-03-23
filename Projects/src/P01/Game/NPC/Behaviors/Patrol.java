package P01.Game.NPC.Behaviors;

import P01.Game.AI.Behavior;
import P01.Game.AI.HierarchicalBehavior;
import P01.Game.AI.Reaction;
import P01.Game.Environment.Environment;
import P01.Game.Environment.EnvironmentAction;
import P01.Game.Environment.EnvironmentEvent;

public class Patrol extends HierarchicalBehavior {

    public Patrol() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.SILENCE, EnvironmentAction.PATROL),
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.APPROACH),
                new Reaction(EnvironmentEvent.NOISE, EnvironmentAction.APPROACH)
        });
    }
}
