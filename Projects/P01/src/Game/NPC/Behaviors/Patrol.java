package Game.NPC.Behaviors;

import Game.AI.Behavior;
import Game.AI.HierarchicalBehavior;
import Game.AI.Reaction;
import Game.Environment.Environment;
import Game.Environment.EnvironmentAction;
import Game.Environment.EnvironmentEvent;

public class Patrol extends HierarchicalBehavior {

    public Patrol() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.SILENCE, EnvironmentAction.PATROL),
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.APPROACH),
                new Reaction(EnvironmentEvent.NOISE, EnvironmentAction.APPROACH)
        });
    }
}
