    . A
	   / \
	  B---C
	   \ /
	   D
In this graph, we have four nodes (A, B, C, D) and five edges connecting them (A-B, A-C, B-C, B-D, C-D). The Adjacency list representation of this graph would be:

Adjacency List:
A: [B, C]
B: [A, C, D]
C: [A, B, D]
D: [B, C]

#### undirected graph

```
 static ArrayList<ArrayList<Integer>> convert_edge_list_to_adjacency_list(Integer n, ArrayList<ArrayList<Integer>> edges) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        for(int i=0; i< n; i++){
            result.add(new ArrayList<Integer>());
        }
        for(int i=0; i< edges.size(); i++){
            int source = edges.get(i).get(0);
            int destination = edges.get(i).get(1);
            result.get(source).add(destination);
            result.get(destination).add(source);
        }
        
        return result;
    }
```

#### directed graph
```
 static ArrayList<ArrayList<Integer>> convert_edge_list_to_adjacency_list(Integer n, ArrayList<ArrayList<Integer>> edges) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        for(int i=0; i< n; i++){
            result.add(new ArrayList<Integer>());
        }
        for(int i=0; i< edges.size(); i++){
            int source = edges.get(i).get(0);
            int destination = edges.get(i).get(1);
            result.get(source).add(destination);
        }
        
        return result;
    }
```
