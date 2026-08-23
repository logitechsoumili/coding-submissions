# Longest Common Prefix

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

 

 **Example 1:** 

```
Input: strs = ["flower","flow","flight"]
Output: "fl"

```

 **Example 2:** 

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```

 

 **Constraints:** 

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters if it is non-empty.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 19.78%)  
**Memory:** 19.2 MB (beats 73.62%)  
**Submitted:** 2026-08-23T08:55:58.864Z  

```py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or first[i] != strs[j][i]:
                    return first[:i]

        return first
```

---

[View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)