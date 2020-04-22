package problems.puzzle.models;

import puzzle.Puzzle;
import search.problem.HeuristicProblem;
import search.engine.tree.State;

public class PuzzleProblem extends HeuristicProblem {

    private PuzzleState puzzle;

    public PuzzleProblem(Puzzle initial_puzzle, Puzzle final_puzzle, PuzzleOperator[] operators) {
        super(new PuzzleState(initial_puzzle), operators);
        this.puzzle = new PuzzleState(final_puzzle);
    }

    @Override
    public double heuristic(State state) {
        PuzzleState puzzle = (PuzzleState) state;
        return puzzle.get_puzzle().distManhattan(this.puzzle.get_puzzle());
    }

    @Override
    public boolean objective(State state) {
        PuzzleState puzzle = (PuzzleState) state;
        return this.puzzle.equals(puzzle);
    }
}
