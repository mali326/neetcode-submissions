from collections import defaultdict

class Solution:
    def checkDup(self, section: List[str]) -> bool:
        seen = set()
        for x in section:
            if x == '.':
                continue
            elif x in seen:
                return True
            else: # if x not . and not in seen, add to seen
                seen.add(x)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hasDup = False #has no duplicate until found

        # rows
        for i in range(9):
            if self.checkDup(board[i]):
                return False

        # cols
        tBoard = [list(row) for row in zip(*board)]
        for i in range(9):
            if self.checkDup(tBoard[i]):
                return False

        # boxes
        boxes = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    x = (i//3) * 3 + (j//3)
                    boxes[x].append(board[i][j])
        for x in range(9):
            if self.checkDup(boxes[x]):
                return False
        
        return True


            

            

