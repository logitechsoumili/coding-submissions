class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        windowSum = 0
        left = 0

        for right in range(len(nums)):
            windowSum += nums[right]

            while windowSum >= target:
                minLen = min(minLen, right - left + 1)
                windowSum -= nums[left]
                left += 1

        return 0 if minLen == float('inf') else minLen