package Game.Environment;

import java.util.HashMap;
import java.util.Map;

public class Environment {

    private Map<String, EnvironmentEvent> events = new HashMap<>();
    private EnvironmentEvent event;

    public Environment() {
        this.events.put("EXIT", EnvironmentEvent.EXIT);
        this.events.put("NOISE", EnvironmentEvent.NOISE);
        this.events.put("SILENCE", EnvironmentEvent.SILENCE);
        this.events.put("ENEMY", EnvironmentEvent.ENEMY);
        this.events.put("FLEE", EnvironmentEvent.FLEE);
        this.events.put("VICTORY", EnvironmentEvent.VICTORY);
        this.events.put("DEFEAT", EnvironmentEvent.DEFEAT);
    }

    public void evolve(String input) {
        this.event = this.generate_event(input);
    }

    private EnvironmentEvent generate_event(String input) {
        return this.events.get(input.toUpperCase());
    }

    public EnvironmentEvent get_event() {
        return this.event;
    }

}
