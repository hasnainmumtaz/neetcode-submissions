import copy
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        # Condition 1
        board_copy = copy.deepcopy(board)
        for row in board_copy:
            while "." in row:
                row.remove(".")
            if len(set(row)) != len(row):
                valid = False
                return valid

        # Condition 2
        #board is transposed
        board = [list(row) for row in zip(*board)]
        board_copy = copy.deepcopy(board)
        for row in board_copy:
            while "." in row:
                row.remove(".")
            if len(set(row)) != len(row):
                valid = False
                return valid
        
        # Condition 3
        for row_id in range(0,8,3):
            rows = board[row_id: row_id+3]
            #print(rows)
            for col_id in range(0,8,3):
                list_box = [row[col_id:col_id+3] for row in rows]
                one_box = []
                for row in list_box:
                    while "." in row:
                        row.remove(".")
                    one_box.extend(row)
                if len(set(one_box)) != len(one_box):
                    valid = False
                    return valid
        return valid
                
