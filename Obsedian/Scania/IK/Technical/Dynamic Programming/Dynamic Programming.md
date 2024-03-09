
DP is doing recursion without repetition.
There are 2 variants
1. Memoization (top-dowm)
2. Tabulation (bottom-up)

Try to find a Bottom-up/ iterative solution

1> Fibonacci series:
	here we have to find the fib series. 
	the formula is  f(n) = f(n-1) + f(n-1);
```
 static Integer find_fibonacci(Integer n) {
        // Write your code here.
        if(n == 1 || n == 2){
            return 1;
        }
        if(n == 0) return 0;
        int prev = 1;
        int curr = 1;
        for(int i= 2; i< n; i++){
            int sum = prev + curr;
            prev = curr;
            curr = sum;
        }
        
        return curr;
    }
```

2. Counting steps / climbing stairs:

![[climbing stairs]]


```
	   static Long jump_ways(Integer n) {
        // Write your code here.
         if(n == 0) return 0L;
        if(n == 1) return 1L;
        if(n == 2) return 2L;
        Long[] dp = new Long[n+1];
        dp[1] = 1L;
        dp[2] = 2L;
        for(int i = 3; i<= n; i++){
            dp[i] = dp[i-2] + dp[i-1];
        }
        return dp[n];
    }

/////// for 1 and 3 steps

	static Long jump_ways(Integer n) {
	    if (n == 0) return 0L;
	    if (n == 1) return 1L;
	    if (n == 2) return 2L;
	
	    Long[] dp = new Long[n + 1];
	    dp[1] = 1L;
	    dp[2] = 2L;
	    dp[3] = 4L; // Initial value for when n = 3
	
	    for (int i = 4; i <= n; i++) {
	        dp[i] = dp[i - 1] + dp[i - 3];
	    }
	    return dp[n];
	}


```

3. Counting subset of size k:

		Formula = c(n.k) = c(n-1, k) + c(n-1, k-1)
	here we can exclude the person from committee C(n-1, k) or include the person in committee C(n-1,k-1) 

	here k < n

![[subset of n choose k]]
		
```
 static Integer ncr(Integer n, Integer r) {
        // Using the modulo operation (% P) is a common practice in dynamic programming algorithms and combinatorics to prevent integer overflow and keep the numbers within a manageable range. 

        final int P = 1000000007;
        int row = n;
        int col = r;
        long[][] dp = new long [row+1][col+1];
        for(int i=0; i<= row; i++){
            dp[i][0] = 1;
        }
        for(int i=0; i<= row; i++){
            for (int j = 1; j <= col && j <= i; j++) {
                dp[i][j] = 1;
            }
        }
        //c(n,k) = c(n-1, k) + c(n-1, k-1))
        for(int i=2; i<= row; i++){
            for(int j= 1; j<= col; j++){
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % P;
            }
        }
        return (int) dp[n][r];
    }

```
### Problems

1.  Unique Path : Given 2d array find how many unique ways you can reach from start to end

| 1 | 1 | 1 | 1 | 1 |
| ---- | ---- | ---- | ---- | ---- |
| 1 | (m-1,n)+(m, n-1) = 1+1 =2 | 3 | 4 | 5 |
| 1 | 3 | 6 | 10 | 15 |
| 1 | 4 | 10 | 20 | 35 |
| 1 | 5 | 15 | 35 | 70 |
| 1 | 6 | 21 | 56 | End = 126 |

```
public void findPath(int m, int n){
	int[][] dp= new int[m][n];
	for(int i=0; i< m; i++){
		dp[i][0] = 1;
	}
	for(int i=0; i< n; i++){
		dp[0][i] = 1;
	}
	for(int i=1; i< m; i++){
		for(int j=1; j< n; j++){
			dp[i][j] = dp[i-1][j] + dp[i][j-1];
		}
	}
	return dp[m][n];
}
```
2. Unique Path 2 : Given 2d array with obstacle find how many unique ways you can reach from start to end

```
public void findPath(int m, int n, int[][] struct){
	int[][] dp= new int[m][n];
	for(int i=0; i< m; i++){
		for(int j=0; j< m; j++){
			dp[i][j] = 0;
		}
	}
	for(int i=0; i< m; i++){
		if(struct[i][0] == 1){
			break; // once obstacle is reached the other column are unreachable and therfore it will be zero
		}
		dp[i][0] = 1;
	}
	for(int i=0; i< n; i++){
		if(struct[0][i] == 1){
			break;
		}
		dp[0][i] = 1;
	}
	for(int i=1; i< m; i++){
		for(int j=1; j< m; j++){
			if(struct[i][j] == 1){
				dp[i][j] = 0;
			}else{
				dp[i][j] = dp[i-1][j] + dp[i][j-1];
			}
			
		}
	}
	return dp[m-1][n-1];
}
```

3. Given a triangle find the minimum path sum from top to bottom
			    2
			    3   4
		     6  5  7
		     4. 1. 8. 3
```


class Solution {

	public int minimumTotal(List<List<Integer>> triangle) {

		int n = triangle.size();

		int[] dp = new int[n];

		for(int i = 1; i< n; i++){
		
			dp[i] = triangle.get(n - 1).get(i);
		
		}

		for(int i= n-2; i>= 0; i--){
		
			for(int j=0; j< i; j++){
			
				dp[j] = Math.min(dp[j], dp[j+1]) + triangle.get(i).get(j);
			
			}
		
		}

		return dp[0];

	}
}

```
Exactly, that's the key idea in the bottom-up dynamic programming approach for this problem. By starting from the bottom and moving upwards, you can iteratively calculate the minimum path sum for each position in the triangle.

The transition for each position `(i, j)` involves taking the current value in the triangle (`triangle.get(i).get(j)`) and adding the minimum of the two possible paths from the row below (`dp[j]` and `dp[j + 1]`). This way, you progressively build up the minimum path sum from the bottom to the top of the triangle.

This approach ensures that, at the end of the process, `dp[0]` will contain the minimum path sum starting from the top of the triangle down to the bottom. It's an efficient way to solve the problem and avoid redundant calculations by memoizing intermediate results.


4. Fibonacci number

		1 1 2 3 5 8 13 ......


