package P01.Game;

import P01.Game.Environment.Environment;
import P01.Game.Environment.EnvironmentEvent;
import P01.Game.NPC.Character;

import java.util.Scanner;

public class Game {

    private Environment environment = new Environment();
    private Character character = new Character(environment);

    public static void main(String[] args) {
        new Game().execute_game();
    }

    private void execute_game() {

        Scanner scanner = new Scanner(System.in);
        EnvironmentEvent event;

        String event_name = "";
        String behavior_name = "";
        String input = "";

        do {
            this.environment.evolve(input);
            event_name = this.environment.show();

            this.character.execute();
            behavior_name = this.character.show();

            System.out.printf("[ %7s @ %-10s ]$ ", event_name, behavior_name);
            input = scanner.next();

            event = environment.get_event();

        } while(event == null ? true : event != EnvironmentEvent.EXIT);
    }
}
