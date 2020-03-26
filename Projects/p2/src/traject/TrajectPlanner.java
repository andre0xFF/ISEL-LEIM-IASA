package traject;

import search_strategies.uninformed.BreadthFirstSearch;
import search_strategies.uninformed.DepthFirstSearch;
import search_strategies.uninformed.IterativeSearch;
import search_strategies.engine.Search;
import search_strategies.problem.Solution;
import search_strategies.problem.SolutionStep;
import traject.models.ConnectionOperator;
import traject.models.TrajectProblemPlanner;

public class TrajectPlanner {

    public static void main(String[] args) {
        ConnectionOperator[] operators = get_operators();

        TrajectProblemPlanner problem = new TrajectProblemPlanner("Loc-0", "Loc-6", operators);
        Search search;
        Solution solution;

        System.out.printf("\n$ Depth First Search\n");

        search = new DepthFirstSearch();
        solution = search.solve(problem);
        show_traject(solution);

        System.out.printf("\n$ Breadth First Search\n");

        search = new BreadthFirstSearch();
        solution = search.solve(problem);
        show_traject(solution);

        System.out.printf("\n$ Iterative Search\n");

        search = new IterativeSearch();
        solution = search.solve(problem);
        show_traject(solution);
    }

    private static ConnectionOperator[] get_operators() {
        return new ConnectionOperator[] {
            new ConnectionOperator("Loc-0", "Loc-1", 5),
            new ConnectionOperator("Loc-0", "Loc-2", 25),
            new ConnectionOperator("Loc-1", "Loc-3", 12),
            new ConnectionOperator("Loc-1", "Loc-6", 5),
            new ConnectionOperator("Loc-2", "Loc-4", 30),
            new ConnectionOperator("Loc-3", "Loc-2", 10),
            new ConnectionOperator("Loc-3", "Loc-5", 5),
            new ConnectionOperator("Loc-4", "Loc-3", 2),
            new ConnectionOperator("Loc-5", "Loc-6", 8),
            new ConnectionOperator("Loc-5", "Loc-4", 10),
            new ConnectionOperator("Loc-6", "Loc-3", 15),
        };
    }

    private static void show_traject(Solution solution) {
        if (solution == null) {
            System.out.println("No solution");
        }

        for (SolutionStep step : solution) {
            System.out.printf("%s (%s)\n", step.get_state().toString(), step.get_cost());
        }
    }
}
