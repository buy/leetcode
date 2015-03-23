# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X

import collections

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    # 2:37
    def solve(self, board):
        if not board or not board[0]:
            return

        rowLength = len(board)
        colLength = len(board[0])

        # convert to real matrix to make life easier ...
        for row in range(rowLength):
            board[row] = list(board[row])
        
        for i in range(colLength):
            self.markEdgeOArea(board, 0, i)
            self.markEdgeOArea(board, rowLength - 1, i)

        for j in range(rowLength):
            self.markEdgeOArea(board, j, 0)
            self.markEdgeOArea(board, j, colLength - 1)

        for i in range(rowLength):
            for j in range(colLength):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == 'K':
                    board[i][j] = 'O'

    def markEdgeOArea(self, board, i, j):
        queue = collections.deque([(i, j)])
        while queue:
            row, col = queue.popleft()
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'O':
                continue
    
            board[row][col] = 'K'
            queue.append((row - 1, col))
            queue.append((row + 1, col))
            queue.append((row, col - 1))
            queue.append((row, col + 1))


s = Solution()
b = ["XOX","OXO","XOX"]
s.solve(b)
print b
