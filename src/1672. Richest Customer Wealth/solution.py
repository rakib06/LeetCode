class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = [sum(int(v) for v in item) for item in accounts]
        return max(total)
