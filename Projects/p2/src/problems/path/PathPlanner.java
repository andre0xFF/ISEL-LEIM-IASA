package problems.path;

import search.uninformed.BreadthFirstSearch;
import search.uninformed.DepthFirstSearch;
import search.uninformed.IterativeSearch;
import search.engine.Search;
import search.problem.Solution;
import search.problem.SolutionStep;
import problems.path.models.ConnectionOperator;
import problems.path.models.PathProblemPlanner;
import search.uninformed.UniformCostSearch;

public class PathPlanner {

	public static void main(String[] args) {
		ConnectionOperator[] operators = get_operators();

		PathProblemPlanner problem = new PathProblemPlanner(
            "Loc-0",
            "Loc-4",
            operators
		);

		run_experiment(new DepthFirstSearch(), problem);
		run_experiment(new BreadthFirstSearch(), problem);
		run_experiment(new IterativeSearch(), problem);
		run_experiment(new UniformCostSearch(), problem);
	}

	private static void run_experiment(Search type, PathProblemPlanner problem) {
		System.out.format("$ %s\n", type);
		Solution solution = type.solve(problem);
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
			System.out.format("%s (%s)\n", step.get_state(), step.get_cost());
		}
	}
}
