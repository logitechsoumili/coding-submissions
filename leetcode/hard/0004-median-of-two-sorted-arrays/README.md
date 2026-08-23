# Median of Two Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return  **the median**  of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

 **Example 1:** 

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

```

 **Example 2:** 

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

```

 

 **Constraints:** 

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 45.92%)  
**Memory:** 19.4 MB (beats 95.48%)  
**Submitted:** 2026-08-23T06:09:39.525Z  

```py
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half - i

            Aleft = nums1[i - 1] if i > 0 else float('-inf')
            Aright = nums1[i] if i < m else float('inf')

            Bleft = nums2[j - 1] if j > 0 else float('-inf')
            Bright = nums2[j] if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2:
                    return (max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                high = i - 1

            else:
                low = i + 1  
```

---

[View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)