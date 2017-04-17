public class BreadthFirstSearch extends SearchMechanism implements Search {

    @Override
    protected SearchMemory start_memory() {
        return new FIFOMemory();
    }
}
