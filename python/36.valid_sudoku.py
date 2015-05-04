# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if not board:
            return False

        row, col, box = [[False] * 9 for i in range(10)], [[False] * 9 for i in range(10)], [[False] * 9 for i in range(10)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num != '.':
                    index = int(num) - 1
                    k = i / 3 * 3 + j / 3
                    if row[i][index] or col[j][index] or box[k][index]:
                        return False

                    row[i][index] = col[j][index] = box[k][index] = True

        return True
