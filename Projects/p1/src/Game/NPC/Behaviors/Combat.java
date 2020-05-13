package game.npc.behaviors;

import game.environment.EnvironmentAction;
import game.environment.EnvironmentEvent;
import machine.intelligence.Behavior;
import machine.intelligence.HierarchicalBehavior;
import machine.intelligence.Reaction;

public class Combat extends HierarchicalBehavior {

    public Combat() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.ATTACK),
                new Reaction(EnvironmentEvent.DEFEAT, EnvironmentAction.START)
        });
    }
}
