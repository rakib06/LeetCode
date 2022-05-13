class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            x = nums.index(target)
            return x
        except:
            return -1
