package P01.Game;

import java.util.Scanner;

public class Game {

    Environment environment = new Environment();
    Character character = new Character(environment);

    public static void main(String[] args) {
        new Game().execute_game();
    }

    private void execute_game() {

        Scanner input = new Scanner(System.in);
        EnvironmentEvent event;

        do {
            System.out.printf("[ Noise / Silence / Enemy @ Environment event]$ ");
            String event_name = input.nextLine();

            this.character.execute();
            this.environment.evolve(event_name);
            event = environment.get_event();

        } while(event != EnvironmentEvent.EXIT);
    }
}
