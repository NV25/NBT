"""
Given a collection of intervals, merge all overlapping intervals.

"""

class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

def mergeIntervals(intervals):

    # Sort by start time
    intervals.sort(key=lambda x: x.start)
    mergedIntervals = []

    for interval in intervals:
        if not mergedIntervals or mergedIntervals[-1].end < interval.start:
            mergedIntervals.append(interval)
            continue

        if mergedIntervals[-1].end >= interval.start:
            previous_interval = mergedIntervals.pop()
            mergedIntervals.append(Interval(previous_interval.start,
                                            max(previous_interval.end, interval.end)))

    return mergedIntervals


if __name__ == "__main__":
    ints = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = []

    for i in ints:
        intervals.append(Interval(i[0], i[1]))

    mergedIntervals = mergeIntervals(intervals)

    for m in mergedIntervals:
        print("{} to {}".format(m.start, m.end))