package puzzle.models;

import puzzle.Puzzle;
import search_strategies.engine.tree.Operator;
import search_strategies.engine.tree.State;
import puzzle.Puzzle.Movimento;

public class PuzzleOperator implements Operator {

    private Movimento movement;
    private float cost;

    public PuzzleOperator(Movimento movement, float cost) {
        this.movement = movement;
        this.cost = cost;
    }

    @Override
    public State apply(State state) {
        PuzzleState puzzle_state = (PuzzleState) state;

        Puzzle puzzle = puzzle_state.get_puzzle().movimentar(this.movement);

        if (puzzle == null) {
            return null;
        }

        return new PuzzleState(puzzle);
    }

    @Override
    public float get_cost(State state, State successor) {
        return this.cost;
    }
}
