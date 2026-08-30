class Solution:
    def isValid(self, squares):
        square_set = set(squares)
        square_set.discard(".")
        if len(square_set) != len(squares) - squares.count("."):
            return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print("Hello")
        for row in board:
            if not self.isValid(row):
                print(row)
                return False
        print("Hello")
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if not self.isValid(column):
                return False
        
        for l in range(3):
            for k in range(3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        cell.append(board[i+3*k][j+3*l])
                print(cell)
                if not self.isValid(cell):
                    return False
        
        return True