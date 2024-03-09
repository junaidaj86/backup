A Binary Search Tree (BST) is a binary tree data structure where each node has at most two child nodes, referred to as the left child and the right child. The key property of a BST is that the value of each node in the left subtree is less than or equal to the node's value, and the value of each node in the right subtree is greater than the node's value.

Time complexity : O(log h+1) = O(log n)

### Searching in tree
````
public TreeNode searchRecursive(TreeNode node, Integer key){
	if(node == null){
		return null;
	} 
	if(node.value == key) {
		return node;
	} 
	if(node.value < key){
		search(node.right, key); // values greater are stored in right side
	}
	if(node.value > key){
		search(node.left, key);
	}
}

````

````
  public TreeNode searchIterative(TreeNode node, Integer key){
	if(node == null){
		return null;
	} 
	while(node != null){
		if(node.value == key) {
			return node;
		} 
		if(node.value < key){
			node = node.right;
		}
		if(node.value > key){
			node = node.left;
		}
	}

	return null;
}
````

### BST Insert
1. search the tree to find where the key fits in
2. keep track of prev and current pointer
3. key is less than prev, then keys goes to prev.left
4. else it goes to prev.right

````

public void insertNode(TreeNode node, Integer key){
	TreeNode newNode = new TreeNode(key);
	if(node == null) return newNode;
	TreeNode curr = node;
	TreeNode prev = null;
	while(curr != null){
		if(key == curr.value){
			System.out.println("key exists);
			return;
		}
		if(key < curr.value){
			prev = curr;
			curr = curr.left;
		}
		if(key > curr.right){
			prev = curr;
			curr = curr.right;
		}
	}
	if(key < prev.value){
		prev.left = newNode;
	}else{
		prev.right = newNode;
	}
	
}
````

### BST min and Max

1. Minimum will always be on the left side of the tree
2. Maximum will always be on the right side of the tree.

###### Finding minimum
````
public Integer findMinimum(TreeNode node, Integer key){
	if(node == null) return null;
	TreeNode curr = node;
	while(curr.left != null){
		curr = curr.left;
	}
	return curr.value;
}
````

###### Finding maximum

````
public Integer findMaximum(TreeNode node, Integer key){
	if(node == null) return null;
	TreeNode curr = node;
	while(curr.right != null){
		curr = curr.right;
	}
	return curr.value;
}
````


### BST successor
- For a given node `N` in a binary search tree, the successor of `N` is the node with the smallest key greater than the key of node `N`.
- If node `N` has a right subtree, the successor is the node with the minimum key in that right subtree.
- If node `N` does not have a right subtree, you need to look up the tree to find the first ancestor where `N` is in the left subtree of that ancestor. The ancestor is then the successor.

````
public TreeNode findSucceesor(TreeNode node, Integer key){
	if(node == null) return null;
	TreeNode curr = node;
	TreeNode succ = null;
	while(curr != null){
		if(curr.value == key){
			return succ;
		}
		if(curr.value < key){
			curr = curr.right;
		}
		if(curr.value > key){
			curr = curr.left;
		}
		return curr.right;
	}
}
````

### BST predecessor
````
public TreeNode findPredecesor(TreeNode node, Integer key){
	if(node == null) return null;
	TreeNode curr = node;
	TreeNode ancestor = null;
	while(curr.key != key){
		if(curr.value > key){
			ancestor = curr;
		}else{
			curr = curr.left;
		}
	}
	return ancestor;
}
````


### BST deletion case 1, case 2, and case 3

If the deletion node is leaf node
````
public TreeNode delete(TreeNode node, Integer key){
	if(node == null) return root;
	TreeNode curr = node;
	TreeNode prev = null;
	while(curr != null){
		if(curr.value < key){
			prev = curr;
			curr = curr.right;
		}else if(curr.value > key){
			prev = curr;
			curr = curr.left;
		}else{
		   . ### BST deletion case 1
			 if(curr.left == null && curr.right == null){
				 if(prev == null) return null;
				 if(curr == prev.left){
					 prev.left = null;
				 }else{
					 prev.right = null;
				 }
			}
			### BST deletion case 2, any one node is null
			else if(curr.left == null || curr.right == null){
				if(curr.left != null){
					if(curr.value > prev.value){
						prev.right = curr.left;
					}else{
						prev.left = curr.left;
					}
				}
				if(curr.right != null){
					if(curr.value > prev.value){
						prev.right = curr.right;
					}else{
						prev.left = curr.right;
					}	
				  }
			}
			### BSR deletion case 3, both left and right and not null
			else{
				# find minimum and replace it with prev of left or right
				TreeNode temp = findMin(curr, key);
				if(prev.value > curr.value){
					prev.left = temp;
				}else{
					prev.right = temp;
				}
			}
	    }
	}
	
	return root;
}

public TreeNode findMin(TreeNode root, Integer value){
	TreeNode curr = curr;
	while(curr.left != null){
		if(curr.value < value){
			curr = curr.right;
		}else (curr.value > value){
			curr = curr.left;
		}else {
			break;
		}
	}
	return curr;
}
````

### BFS

````
public ArrayList<Integer> bfs(TreeNode root){
	if(root == null) return new ArrayList<Integer>();
	Queue<TreeNode> q = new LinkedList<>();
	q.add(root);
	ArrayList<Integer> result = new ArrayList<Integer>();
	while(!q.isEmpty()){
		TreeNode temp = q.remove();
		resilt.add(temp.value);
		if(temp.left != null){
			q.add(temp.left);
		}else if(temp.right != null){
			q.add(temp.right);
		}
	}
return result;
}
````

### DFS
#### preorder

````
public ArrayList<Integer> dfs(TreeNode node, ArrayList<Integer> result){
	result.add(node.value);
	dfs(node.left, result);
	dfs(node.right, result);
}
````

#### inorder
````
public ArrayList<Integer> dfs(TreeNode node, ArrayList<Integer> result){
	dfs(node.left, result);
	result.add(node.value);
	dfs(node.right, result);
}
````

#### post order
````
public ArrayList<Integer> dfs(TreeNode node, ArrayList<Integer> result){
	dfs(node.left, result);
	dfs(node.right, result);
	result.add(node.value);
}
````
