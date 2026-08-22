# Minimum Size Subarray Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return  *the  **minimal length**  of a  **subarray**  whose sum is greater than or equal to*  `target`. If there is no such subarray, return `0` instead.

 

 **Example 1:** 

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

 **Example 2:** 

```
Input: target = 4, nums = [1,4,4]
Output: 1

```

 **Example 3:** 

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```

 

 **Constraints:** 

- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Solution

**Language:** Python  
**Runtime:** 14 ms (beats 90.43%)  
**Memory:** 30.5 MB (beats 78.83%)  
**Submitted:** 2026-08-22T09:51:35.660Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)