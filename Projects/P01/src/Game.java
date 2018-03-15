import Game.Environment.Environment;
import Game.Environment.EnvironmentEvent;
import Game.NPC.Character;

import java.util.Scanner;

public class Game {

    private static Environment environment = new Environment();
    private static Character character = new Character(environment);

    public static void main(String[] args) {
        execute_game();
    }

    private static void execute_game() {

        Scanner scanner = new Scanner(System.in);
        EnvironmentEvent event;

        do {
            System.out.print("\nEvent: ");
            String input = scanner.next();

            environment.evolve(input);
            character.execute();

            String state = character.show();
            System.out.print(String.format("State: %s\n", state));

            event = environment.get_event();

        } while(event == null || event != EnvironmentEvent.EXIT);
    }
}
