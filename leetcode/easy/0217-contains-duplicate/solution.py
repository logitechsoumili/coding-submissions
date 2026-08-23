from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        f = Counter(nums)

        for i in f.values():
            if i >= 2:
                return True

        return False