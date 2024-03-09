.         A
     / \
   .   B---C
    \ / \
    D

In this graph, we have four nodes (A, B, C, D) and five edges connecting them (A-B, A-C, B-C, B-D, C-D). The Adjacency matrix representation of this graph would be:

A  B  C  D
A  0  1  1  0
B  1  0  1  1
C  1  1  0  1
D  0  1  1  0

#### undirected graph

```

    static ArrayList<ArrayList<Boolean>> convert_edge_list_to_adjacency_matrix(Integer n, ArrayList<ArrayList<Integer>> edges) {
        ArrayList<ArrayList<Boolean>> result = new ArrayList<ArrayList<Boolean>>();
        for(int i =0; i< n; i++){
             ArrayList<Boolean> row = new ArrayList<>(Collections.nCopies(n, false));
            result.add(row);
        }
        for(int i=0; i< edges.size(); i++){
            int source = edges.get(i).get(0);
            int destination = edges.get(i).get(1);
            result.get(source).set(destination, true);
            result.get(destination).set(source, true);
        }
        return result;
    }

```

#### directed graph
```

    static ArrayList<ArrayList<Boolean>> convert_edge_list_to_adjacency_matrix(Integer n, ArrayList<ArrayList<Integer>> edges) {
        ArrayList<ArrayList<Boolean>> result = new ArrayList<ArrayList<Boolean>>();
        for(int i =0; i< n; i++){
             ArrayList<Boolean> row = new ArrayList<>(Collections.nCopies(n, false));
            result.add(row);
        }
        for(int i=0; i< edges.size(); i++){
            int source = edges.get(i).get(0);
            int destination = edges.get(i).get(1);
            result.get(source).set(destination, true);
        }
        return result;
    }
```