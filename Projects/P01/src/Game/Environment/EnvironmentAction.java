package Game.Environment;

import Game.AI.Action;

public enum EnvironmentAction implements Action {
    PATROL, DEFEND, START, SEARCH, ATTACK, WARN, APPROACH;

    @Override
    public void execute() {
        // TODO
    }
}
