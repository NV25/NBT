"""
Given an array of meeting time intervals consisting of
start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.


"""

import heapq

class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x.start)
    roomHeap = []

    for interval in intervals:
        if roomHeap and roomHeap[0] <= interval.start:
            heapq.heappop(roomHeap)

        heapq.heappush(roomHeap, interval.end)

    return len(roomHeap)

if __name__ == "__main__":
    ints = [[0, 30],[5, 10],[15, 20]]
    intervals = []

    for i in ints:
        intervals.append(Interval(i[0], i[1]))

    print(minMeetingRooms(intervals))
