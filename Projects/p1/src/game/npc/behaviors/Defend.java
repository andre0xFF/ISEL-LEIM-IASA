package game.npc.behaviors;

import game.environment.EnvironmentAction;
import game.environment.EnvironmentEvent;
import machine.intelligence.Behavior;
import machine.intelligence.HierarchicalBehavior;
import machine.intelligence.Reaction;

public class Defend extends HierarchicalBehavior {

    public Defend() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.DEFEND)
        });
    }
}
