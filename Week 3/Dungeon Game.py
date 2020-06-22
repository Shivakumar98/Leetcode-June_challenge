The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3    	3
-5	    -10	    1
10	     30	    -5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        d=dungeon
        # Actual Height and Width
        h,w=len(d),len(d[0])
        
        #We will track for h-1 and w-1 
        m,n=h-1,w-1
        
        # Minimum should be 1 or 1-last element
        d[m][n]=max(1,1-d[m][n])
        
        # checking for last row of dungeons
        for row in range(m-1,-1,-1):
            d[row][n]=max(1,d[row+1][n]-d[row][n])
        
        # checking for last col of dungeons
        for col in range(n-1,-1,-1):
            d[m][col]=max(1,d[m][col+1]-d[m][col])
        
        # Now finding respective minmum between col end and row end
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                d[row][col]=max(1,min(d[row+1][col],d[row][col+1])-d[row][col])
        
        print(d)
        print(d[0][0])
        
        return d[0][0]
        
        
