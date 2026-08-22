# attend-all-meetings-ii

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-22T09:31:02.866Z  

```py
class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        
        i, j = 0, 0
        active, rooms = 0, 0
        
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                active += 1
                i += 1
                rooms = max(rooms, active)
                
            elif end[j] <= start[i]:
                active -= 1
                j += 1
                
        return rooms
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/attend-all-meetings-ii/1)