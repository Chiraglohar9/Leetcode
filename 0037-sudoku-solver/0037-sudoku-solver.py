from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Pre-fill sets and collect empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def get_candidates(r: int, c: int) -> list:
            used = rows[r] | cols[c] | boxes[(r // 3) * 3 + (c // 3)]
            return [d for d in "123456789" if d not in used]

        def backtrack(idx: int) -> bool:
            if idx == len(empties):
                return True  # all filled

            # Choose next empty cell (you can improve this by reordering, but this often passes)
            r, c = empties[idx]
            candidates = get_candidates(r, c)

            for d in candidates:
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[(r // 3) * 3 + (c // 3)].add(d)

                if backtrack(idx + 1):
                    return True

                # Undo
                board[r][c] = '.'
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[(r // 3) * 3 + (c // 3)].remove(d)

            return False

        backtrack(0)