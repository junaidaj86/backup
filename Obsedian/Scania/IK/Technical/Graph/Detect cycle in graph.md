```
import java.util.ArrayList;
import java.util.Collections;

public class CycleDetection {

    static boolean hasCycle(int numberOfVertices, int numberOfEdges, ArrayList<ArrayList<Integer>> edges) {
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>(numberOfVertices);
        for (int i = 0; i < numberOfVertices; i++) {
            adjList.add(new ArrayList<>());
        }

        for (ArrayList<Integer> edge : edges) {
            int source = edge.get(0);
            int destination = edge.get(1);
            adjList.get(source).add(destination);
        }

        ArrayList<Integer> visited = new ArrayList<>(Collections.nCopies(numberOfVertices, -1));

        for (int i = 0; i < numberOfVertices; i++) {
            if (visited.get(i) == -1 && isCycle(i, adjList, visited)) {
                return true;
            }
        }

        return false;
    }

    static boolean isCycle(int source, ArrayList<ArrayList<Integer>> adjList, ArrayList<Integer> visited) {
        visited.set(source, 1);
        for (Integer neighbour : adjList.get(source)) {
            if (visited.get(neighbour) == -1) {
                if (isCycle(neighbour, adjList, visited)) {
                    return true;
                }
            } else if (parent.get(source) != neighbour) {
                return true;
            }
        }
        visited.set(source, 2);
        return false;
    }

    public static void main(String[] args) {
        // Example usage
        int numberOfVertices = 4;
        int numberOfEdges = 4;
        ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
        edges.add(new ArrayList<>(List.of(0, 1)));
        edges.add(new ArrayList<>(List.of(1, 2)));
        edges.add(new ArrayList<>(List.of(2, 3)));
        edges.add(new ArrayList<>(List.of(3, 0)));

        boolean hasCycle = hasCycle(numberOfVertices, numberOfEdges, edges);
        System.out.println("Graph has cycle: " + hasCycle);
    }
}


```
