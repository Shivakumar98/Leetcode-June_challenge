Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


class Solution:
    def numSquares(self, n: int) -> int:
        # one thing I learnt from this problem is that we should not "print(list)"
        
        sq=[]
        i,j=1,1
        while j<=n:
            sq.append(j)
            i+=1
            j=i**2
            
        # print(sq)
        # Dynamic programming problem
        dp=[float('inf') for i in range(n+1)]
        # print(dp)
        
        for i in sq:
            for j in range(1,n+1):
                if i<=j:
                    if j%i==0:
                        dp[j]=min((j//i),dp[j])
                    else:
                        dp[j]=min((1+dp[j-i]),dp[j])
                        
        # print(dp)
        # print(dp[n])
        return dp[n]
                
