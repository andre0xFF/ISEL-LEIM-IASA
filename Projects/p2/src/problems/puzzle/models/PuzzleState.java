package problems.puzzle.models;

import puzzle.Puzzle;
import search.engine.tree.State;

public class PuzzleState extends State {

    private Puzzle puzzle;

    public PuzzleState(Puzzle puzzle) {
        this.puzzle = puzzle;
    }

    @Override
    public int hashCode() {
        return this.puzzle.hashCode();
    }

    @Override
    public String toString() {
        return this.puzzle.toString();
    }

    public Puzzle get_puzzle() {
        return this.puzzle;
    }
}
