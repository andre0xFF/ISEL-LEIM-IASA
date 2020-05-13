package game.npc.behaviors;

import machine.intelligence.Behavior;
import machine.intelligence.HierarchicalBehavior;
import machine.intelligence.Reaction;
import game.environment.EnvironmentAction;
import game.environment.EnvironmentEvent;

public class Inspection extends HierarchicalBehavior {

    public Inspection() {
        super(new Behavior[] {
                new Reaction(EnvironmentEvent.NOISE, EnvironmentAction.SEARCH),
                new Reaction(EnvironmentEvent.ENEMY, EnvironmentAction.APPROACH)
        });
    }
}
