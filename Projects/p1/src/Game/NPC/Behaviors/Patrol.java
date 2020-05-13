package game.npc.behaviors;

import machine.intelligence.Behavior;
import machine.intelligence.HierarchicalBehavior;
import machine.intelligence.Reaction;
import game.environment.EnvironmentAction;
import game.environment.EnvironmentEvent;

public class Patrol extends HierarchicalBehavior {

    public Patrol() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.SILENCE, EnvironmentAction.PATROL),
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.APPROACH),
                new Reaction(EnvironmentEvent.NOISE, EnvironmentAction.APPROACH)
        });
    }
}
