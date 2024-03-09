Depth first search

```

    static ArrayList<Integer> dfs_traversal(Integer n, ArrayList<ArrayList<Integer>> edges) {
        // Write your code here.
       ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 0; i < edges.size(); i++) {
            int source = edges.get(i).get(0);
            int destination = edges.get(i).get(1);
            adjList.get(source).add(destination);
            adjList.get(destination).add(source);
        }

        ArrayList<Boolean> visited = new ArrayList<>(Collections.nCopies(n, false));
        ArrayList<Integer> captured = new ArrayList<>();
		int component = 0;
        for (int node = 0; node < n; node++) {
	        component ++;
            if (!visited.get(node)) {
                
                dfs(node, adjList, visited, captured);
               
            }
        }

        return captured;

    }
    
    static void dfs(int node, ArrayList<ArrayList<Integer>> adjList, ArrayList<Boolean> visited, ArrayList<Integer> captured) {
        visited.set(node, true);
        captured.add(node);

        for (Integer neighbor : adjList.get(node)) {
            if (!visited.get(neighbor)) {
                dfs(neighbor, adjList, visited, captured);
            }
        }
    }


```
