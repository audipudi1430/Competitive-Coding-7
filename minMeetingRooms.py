# Approach:
# - Sort the meetings by start time to process them in chronological order.
# - Use a Min-Heap to keep track of end times of ongoing meetings.
# - If a meeting can reuse a room (heap top <= meeting start), pop it; otherwise, allocate a new room.
#
# Time Complexity: O(n log n), dominated by sorting and heap operations (heap push/pop are O(log n) for each of n intervals).
# Space Complexity: O(n), for storing all meeting end times in the heap.

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])  # Sort by start time
        
        minHeap = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)  # Reuse a room
            
            heapq.heappush(minHeap, end)  # Allocate a new room
        
        return len(minHeap)
