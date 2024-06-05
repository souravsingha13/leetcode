class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rows = len(accounts)
        columns = len(accounts[0]) if rows > 0 else 0
        max_wealth = 0
        row_sum = 0
        for i in range(rows):
            for j in range(columns):
                row_sum += accounts[i][j]
            if max_wealth < row_sum:
                max_wealth = row_sum
            row_sum = 0
        return max_wealth