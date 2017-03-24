package P01.Game.NPC;

import P01.Game.AI.Action;
import P01.Game.AI.CharacterBehavior;
import P01.Game.AI.Stimulus;
import P01.Game.Environment.Environment;

public class Character {

    private final Environment environment;
    private CharacterBehavior behavior;

    public Character(Environment environment) {
        this.environment = environment;
        this.behavior = new CharacterBehavior();
    }

    public void execute() {
        Stimulus stimulus = this.percept();

        if (stimulus != null) {
            Action action = this.process(stimulus);
            this.behave(action);
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

    public String show() {
        return String.format("%s", this.behavior.get_state().get_name());
    }
}
