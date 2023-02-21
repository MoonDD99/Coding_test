from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowValid = [[False for _ in range(10)] for _ in range(9)]
        colValid = [[False for _ in range(10)] for _ in range(9)]
        subBoxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                element = board[row][col]
                if element == ".":
                    continue
                element = int(element)
                if rowValid[row][element] or colValid[col][element] or element in subBoxes[(int(row/3),int(col/3))]:
                    return False
                rowValid[row][element] = True
                colValid[col][element] = True
                subBoxes[(int(row/3),int(col/3))].add(element)
        
        return True
