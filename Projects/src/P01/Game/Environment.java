package P01.Game;

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
    }

    public void evolve(String input) {
        this.event = this.events.get(input.toUpperCase());
        // TODO: show ??
    }

    public EnvironmentEvent get_event() {
        return this.event;
    }

    private void show() {
        // TODO: No idea what this shit does.
    }
}

enum EnvironmentEvent implements Stimulus {
    EXIT, NOISE, SILENCE, ENEMY
}

interface Stimulus {}