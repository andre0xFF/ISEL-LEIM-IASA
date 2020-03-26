package Game.Environment;

import Game.AI.Action;

public enum EnvironmentAction implements Action {
    PATROL, DEFEND, START, SEARCH, ATTACK, APPROACH;

    @Override
    public void execute() {
        System.out.print(String.format("Action: %s\n", this));
    }
}
