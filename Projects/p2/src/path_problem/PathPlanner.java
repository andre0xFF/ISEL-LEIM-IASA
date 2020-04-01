package path_problem;

import search.uninformed.BreadthFirstSearch;
import search.uninformed.DepthFirstSearch;
import search.uninformed.IterativeSearch;
import search.engine.Search;
import search.problem.Solution;
import search.problem.SolutionStep;
import path_problem.models.ConnectionOperator;
import path_problem.models.PathProblemPlanner;

public class PathPlanner {

	public static void main(String[] args) {
		ConnectionOperator[] operators = get_operators();

		PathProblemPlanner problem = new PathProblemPlanner(
            "Loc-0",
            "Loc-6",
            operators
		);

		Search search;
		Solution solution;

		System.out.format("\n$ Depth First Search\n");

		search = new DepthFirstSearch();
		solution = search.solve(problem);
		show_path(solution);

		System.out.format("\n$ Breadth First Search\n");

		search = new BreadthFirstSearch();
		solution = search.solve(problem);
		show_path(solution);

		System.out.format("\n$ Iterative Search\n");

		search = new IterativeSearch();
		solution = search.solve(problem);
		show_path(solution);
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

	private static void show_path(Solution solution) {
		if (solution == null) {
			return;
		}

		for (SolutionStep step : solution) {
			System.out.format("%s (%s)\n", step.get_state().toString(), step.get_cost());
		}
	}
}
