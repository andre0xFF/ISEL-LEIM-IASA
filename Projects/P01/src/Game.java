import Game.Environment.Environment;
import Game.Environment.EnvironmentEvent;
import Game.NPC.Character;

import java.util.Scanner;

public class Game {

    private Environment environment = new Environment();
    private Character character = new Character(environment);

    public static void main(String[] args) {
        // TODO: remove new Game(), make it static
        new Game().execute_game();
    }

    private void execute_game() {

        Scanner scanner = new Scanner(System.in);
        EnvironmentEvent event;

        String event_name = "";
        String behavior_name = "";
        String input = "";

        String output_format = "[ %11s @ %-10s ]$ ";
        System.out.printf(output_format + "\n", "ENVIRONMENT", "CHARACTER");

        do {
            this.environment.evolve(input);
            this.character.execute();

            event_name = this.environment.show();
            behavior_name = this.character.show();

            System.out.printf(output_format, event_name, behavior_name);

            event = environment.get_event();

            input = scanner.next();
        } while(event == null ? true : event != EnvironmentEvent.EXIT);
    }
}
