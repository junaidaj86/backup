breadth first search or level order traversal

We use Queue data structure

```
static ArrayList<ArrayList<Integer>> bfs(Integer n, ArrayList<ArrayList<Integer>> edges) {
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<ArrayList<Integer>>();
        Arraylist<Integer> result = new ArrayList<Integer>();
        for(int i=0; i< n; i++){
            adjList.add(new ArrayList<Integer>());
        }
        for(int i=0; i< edges.size(); i++){
            int source = edges.get(i).get(0);
            int destination = edges.get(i).get(1);
            adjList.get(source).add(destination);
            adjList.get(destination).add(source);
        }
        Arraylist<Integer> visited = new ArrayList<Integer>(Collctions.nCopies(n, -1));
        Arraylist<Integer> parent = new ArrayList<Integer>(Collctions.nCopies(n, -1));
        Queue<Integer> q = new LinkedList<Queue>();
        
        int componenet = 0;
    for(int i= 0; i< n; i++){
	    if(visited.get(i) == -1){
	    q.add(i);
	    componenet++;
		    bfs(i, adjList, visited, parent, result);
	    }
    }
		
        
        
        return result;
    }
public void bfs(int source, ArrayList<ArrayList<Integer>> adjList, Arraylist<Integer> visited, Arraylist<Integer> parent, Arraylist<Integer> result){
	while(!q.isEmpty()){
		int temp = q.remove();
		result.add(temp);
		visited.set(i, 1);
		for(int neigh : adjList.get(temp)){
			if(visted.get(neigh) == -1){
				q.add(neigh);
				parent.set(neigh, temp);
			}
		}
	}
}
```


