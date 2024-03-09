**A graph is said to be bipartite if its vertices can be partitioned into two disjoint sets such that every edge connects a vertex from one set to a vertex in the other set. In other words, there are no edges that connect vertices within the same set.**

We can use colouring method to find if a graph is bipartite

````
import java.util.*;

public class BipartiteGraph {
    
    public boolean isBipartite(int n, ArrayList<ArrayList<Integer>> edges) {

        ArrayList<ArrayList<Integer>> adjList = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<Integer>());
        }
        
        for (int i = 0; i < edges.size(); i++) {
            int source = edges.get(i).get(0);
            int destination = edges.get(i).get(1);
            adjList.get(source).add(destination);
            adjList.get(destination).add(source);
        }

        ArrayList<String> color = new ArrayList<>(Collections.nCopies(n, ""));
        ArrayList<Integer> visited = new ArrayList<>(Collections.nCopies(n, -1));
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            if (visited.get(i) == -1) {
                q.add(i);
                visited.set(i, 1);
                color.set(i, getColor(color.get(i)));

                while (!q.isEmpty()) {
                    Integer temp = q.remove();
                    for (Integer neigh : adjList.get(temp)) {
                        if (visited.get(neigh) == -1) {
                            color.set(neigh, giveColor(color.get(temp)));
                            visited.set(neigh, 1);
                            q.add(neigh);
                        } else {
                            if (color.get(neigh).equals(color.get(temp))) {
                                return false;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }

    public String giveColor(String color) {
        if (color.isEmpty())
            return "red";
        else if (color.equals("red"))
            return "blue";
        else
            return "red";
    }
}

````


