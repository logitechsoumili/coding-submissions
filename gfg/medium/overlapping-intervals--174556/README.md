# overlapping-intervals--174556

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-22T09:29:43.981Z  

```py
class Solution:
    def isIntersect(self, intervals):
        intervals.sort()
    
        start1, end1 = intervals[0]
    
        flag = False
    
        for i in range(1, len(intervals)):
            start2, end2 = intervals[i]
    
            if end1 >= start2:
                flag = True
                break
    
            start1, end1 = start2, end2
    
        return flag
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/overlapping-intervals--174556/1)