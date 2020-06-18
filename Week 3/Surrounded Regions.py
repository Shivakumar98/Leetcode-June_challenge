Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we will have 3 types of states
        # 0 = untouched
        # 1 = touched
        # 2 = finished
        
        rows=len(board)
        if rows==0:
            return
        cols=len(board[0])
        if cols==0:
            return
        
        # we will capture the states 
        state = [[0]*cols for i in range(rows)]
        print(state)
        
        # dfs for checking O reaches board edges
        def dfs(x,y,pending):
            #append the pending index
            pending.append((x,y))
            canReach=False            
            
            # defining directions
            dir = [(1,0),(-1,0),(0,1),(0,-1)]
            for dx,dy in dir:
                nextX,nextY=dx+x,dy+y
                
                if nextX<0 or nextX>=rows or nextY<0 or nextY>=cols:
                    canReach=True
                    continue
                if board[nextX][nextY]=="O" and state[nextX][nextY]==0:
                    state[nextX][nextY]==1
                    canReach != dfs(nextX,nextY,pending)
            print(canReach)
            return canReach
        
        
        # we will traverse to every rows and col
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and state[i][j]==0:
                    # var for index which states are changed
                    pending=[]
                    if not dfs(i,j,pending):    #checking whether it can reach outside
                        # change the states from O to X
                        for x,y in pending:
                            board[x][y]="X"
                    for x,y in pending:
                        state[x][y]=2
                        
        print(pending)            
