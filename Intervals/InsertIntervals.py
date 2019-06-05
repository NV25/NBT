"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""

# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


def insertInterval(intervals, newInterval):
    if not newInterval:
        return intervals
    if not intervals:
        return [newInterval]

    i = 0
    # Find position to insert
    while i < len(intervals):
        if intervals[i].start > newInterval.start:
            break
        i += 1

    intervals.insert(i, newInterval)

    # Merge intervals
    return mergeIntervals(intervals)

def mergeIntervals(intervals):
    mergedInt = []

    for interval in intervals:
        if not mergedInt or mergedInt[-1].end < interval.start:
            mergedInt.append(interval)
            continue

        if mergedInt[-1].end >= interval.start:
            previousInt = mergedInt.pop()
            mergedInt.append(Interval(previousInt.start,
                                      max(previousInt.end, interval.end)))

    return mergedInt

def printIntervals(intervals):
    for i in intervals:
        print("{} to {}".format(i.start, i.end))


if __name__ == "__main__":
    ints = [[1,3],[6,9]]
    newInt = [2,5]
    intervals = []

    for i in range(len(ints)):
        intervals.append(Interval(ints[i][0], ints[i][1]))

    newInterval = Interval(newInt[0], newInt[1])
    result = insertInterval(intervals, newInterval)
    printIntervals(result)
