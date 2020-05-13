import game.environment.Environment;
import game.environment.EnvironmentEvent;
import game.npc.Character;

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

            event = environment.get_event();

        } while(event == null || event != EnvironmentEvent.EXIT);

        scanner.close();
    }
}
