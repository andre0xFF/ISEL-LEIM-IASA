package P01.Game.Environment;

import java.util.HashMap;
import java.util.Map;

public class Environment {

    private Map<String, EnvironmentEvent> events;
    private EnvironmentEvent event;

    public Environment() {
        this.events = new HashMap<>();

        // Populate environment events
        this.events.put("EXIT", EnvironmentEvent.EXIT);
        this.events.put("NOISE", EnvironmentEvent.NOISE);
        this.events.put("SILENCE", EnvironmentEvent.SILENCE);
        this.events.put("ENEMY", EnvironmentEvent.ENEMY);
        this.events.put("FLEE", EnvironmentEvent.FLEE);
        this.events.put("VICTORY", EnvironmentEvent.VICTORY);
        this.events.put("DEFEAT", EnvironmentEvent.DEFEAT);
    }

    public void evolve(String input) {
        this.event = this.events.get(input.toUpperCase());
        // TODO: show ??
    }

    public EnvironmentEvent get_event() {
        return this.event;
    }

    public String show() {
        if (this.event != null) {
            return String.format("%s", this.event);
        }
        else {
            return "";
        }
    }

    public void execute_action(EnvironmentAction action) {
        if (action != null) {
            action.execute();
        }
    }
}