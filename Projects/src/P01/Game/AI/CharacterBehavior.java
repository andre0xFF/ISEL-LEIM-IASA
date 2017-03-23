package P01.Game.AI;

import P01.Game.Environment.EnvironmentEvent;
import P01.Game.NPC.Behaviors.Attack;
import P01.Game.NPC.Behaviors.Defend;
import P01.Game.NPC.Behaviors.Inspection;
import P01.Game.NPC.Behaviors.Patrol;
import P01.StateMachine.State;
import P01.StateMachine.StateMachine;

public class CharacterBehavior extends StateMachineBehavior {

    @Override
    protected StateMachine<Stimulus> start() {
        State<Stimulus> patrol = new State<Stimulus>("PATROL");
        State<Stimulus> inspection= new State<Stimulus>("INSPECTION");
        State<Stimulus> defend = new State<Stimulus>("DEFEND");
        State<Stimulus> attack = new State<Stimulus>("ATTACK");

        patrol.add_transition(EnvironmentEvent.ENEMY, defend);
        patrol.add_transition(EnvironmentEvent.NOISE, inspection);

        inspection.add_transition(EnvironmentEvent.ENEMY, defend);
        inspection.add_transition(EnvironmentEvent.SILENCE, patrol);

        defend.add_transition(EnvironmentEvent.FLEE, inspection);
        defend.add_transition(EnvironmentEvent.ENEMY, attack);

        attack.add_transition(EnvironmentEvent.ENEMY, attack);
        attack.add_transition(EnvironmentEvent.FLEE, patrol);
        attack.add_transition(EnvironmentEvent.VICTORY, patrol);
        attack.add_transition(EnvironmentEvent.DEFEAT, patrol);

        super.add_behavior(patrol, new Patrol());
        super.add_behavior(inspection, new Inspection());
        super.add_behavior(defend, new Defend());
        super.add_behavior(attack, new Attack());

        return new StateMachine<Stimulus>(patrol);
    }
}
