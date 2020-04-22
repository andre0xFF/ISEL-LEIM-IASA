package problems.puzzle;

import puzzle.Puzzle;
import problems.puzzle.models.PuzzleOperator;
import problems.puzzle.models.PuzzleProblem;
import search.informed.AStarSearch;
import search.informed.GreedyBestFirstSearch;
import search.uninformed.UniformCostSearch;
import search.uninformed.BreadthFirstSearch;
import search.uninformed.DepthFirstSearch;
import search.uninformed.IterativeSearch;
import search.engine.SearchMechanism;
import search.problem.Solution;
import search.problem.SolutionStep;

public class PuzzleSolver {

    public final static String LINE_FORMAT = "| %-25s | %6s | %15s | %21s | %19s |\n";

    public static void main(String[] args) {
        String s = String.format(
            LINE_FORMAT,
            "Search type",
            "Puzzle",
            "Cost",
            "Max nodes in frontier",
            "Max nodes expanded"
        );

        System.out.format(s);

        Puzzle puzzle_a = new Puzzle(
            new int[][] {
                {1, 2, 3},
                {8, 4, 5},
                {6, 7, 0}
            }
        );

        Puzzle puzzle_b = new Puzzle(
            new int[][] {
                {8, 4, 5},
                {6, 1, 2},
                {3, 7, 0}
            }
        );

        Puzzle puzzle_solution = new Puzzle(
            new int[][] {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 0}
            }
        );

        SearchMechanism[] search_list = {
            new BreadthFirstSearch(),
            new UniformCostSearch(),
            new DepthFirstSearch(),
            new IterativeSearch(),
            new GreedyBestFirstSearch(),
            new AStarSearch(),
        };

        for (SearchMechanism search : search_list) {
            run_search(search, puzzle_a, puzzle_solution, "A");
            run_search(search, puzzle_b, puzzle_solution, "B");
        }
    }

    public static void run_search(SearchMechanism search, Puzzle puzzle, Puzzle goal_puzzle, String name) {
        PuzzleOperator[] operators = new PuzzleOperator[] {
            new PuzzleOperator(Puzzle.Movimento.BAIXO, 1),
            new PuzzleOperator(Puzzle.Movimento.CIMA, 1),
            new PuzzleOperator(Puzzle.Movimento.ESQ, 1),
            new PuzzleOperator(Puzzle.Movimento.DIR, 1)
        };

        PuzzleProblem p = new PuzzleProblem(puzzle, goal_puzzle, operators);

        Solution s = search.solve(p);
        show_puzzle(search, s, name);
    }

    private static void show_puzzle(SearchMechanism search, Solution solution, String puzzle_name) {
        if (solution == null) {
            String s = String.format(
                LINE_FORMAT,
                search.get_title(),
                puzzle_name,
                "",
                "",
                ""
            );

            System.out.format("%s", s);
            return;
        }

        double cost = 0;

        for (SolutionStep step : solution) {
            cost = step.get_cost();
        }

        String s = String.format(
            LINE_FORMAT,
            search.get_title(),
            puzzle_name,
            cost,
            search.get_search_memory().get_max_frontier_nodes(),
            search.get_search_memory().get_max_expanded_nodes()
        );

        System.out.format(s);
    }
}
