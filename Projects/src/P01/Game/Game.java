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

        Scanner input = new Scanner(System.in);
        EnvironmentEvent event;

        do {
            System.out.printf("[ Noise / Silence / Enemy @ Environment event]$ ");
            String event_name = input.nextLine();

            this.environment.evolve(event_name);
            this.character.execute();
            event = environment.get_event();

        } while(event == null ? true : event != EnvironmentEvent.EXIT);
    }
}
