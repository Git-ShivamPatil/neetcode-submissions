class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, ch in enumerate(nums):
            tgt = target - ch
            if tgt in s:
                return [s[tgt], i]

            s[ch] = i
        