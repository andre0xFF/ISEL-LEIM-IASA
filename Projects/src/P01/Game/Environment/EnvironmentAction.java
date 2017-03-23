package P01.Game.Environment;

import P01.Game.AI.Action;

public enum EnvironmentAction implements Action {
    PATROL, DEFEND, START, SEARCH, ATTACK, WARN, APPROACH;

    @Override
    public void execute() {
        // TODO
    }
}
