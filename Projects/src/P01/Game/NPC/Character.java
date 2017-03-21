package P01.Game.NPC;

import P01.Game.Environment.Environment;

public class Character {

    private final Environment environment;

    public Character(Environment environment) {
        this.environment = environment;
    }

    public void execute() {
        Stimulus stimulus = this.percept();

        if (stimulus != null) {
            Action action = this.process(stimulus);
            this.behave(action);
            // TODO: show ??
        }
    }

    // Stimulus is an interface impleted in Action
    private Stimulus percept() {
        return this.environment.get_event();
    }

    private Action process(Stimulus stimulus) {
        // TODO: Transform the Stimulus into some sort of Action
        return null;
    }

    private void behave(Action action) {
        action.execute();
    }
}
