package Game.NPC;

import Game.AI.Action;
import Game.Environment.Stimulus;
import Game.Environment.Environment;

public class Character {

    private final Environment environment;
    private final CharacterBehavior behavior;

    public Character(Environment environment) {
        this.environment = environment;
        this.behavior = new CharacterBehavior();
    }

    public void execute() {
        Stimulus stimulus = this.percept();

        if (stimulus != null) {
            Action action = this.process(stimulus);
            this.behave(action);
            this.show();
        }
    }

    private Stimulus percept() {
        return this.environment.get_event();
    }

    private Action process(Stimulus stimulus) {
        return this.behavior.activate(stimulus);
    }

    private void behave(Action action) {
        if(action != null) {
            action.execute();
        }
    }

    private void show() {
        System.out.printf("State: %s\n", this.behavior.get_state().get_name());
    }
}
