"""
Given an array of integers, find all triplets that add up to a target sum
Time: O(n^2)
Space: O(n)
"""

def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    target_sum = 0

    for i in range(len(nums)):
        n1 = nums[i]
        int_sum = target_sum - n1
        pairs = []
        rest = [nums[n] for n in range(len(nums)) if n != i]

        pairs = TwoSum(rest, int_sum)
        if pairs:
            for p in pairs:
                res.append([n1] + p)

    res = remove_duplicates(res)
    return res


def TwoSum(nums, target):
    res = []
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen.keys():
            complementary_idx = seen[nums[i]]
            res.append([nums[i], nums[complementary_idx]])
        else:
            diff = target - nums[i]
            seen[diff] = i

    res = remove_duplicates(res)
    return res


def remove_duplicates(lists):
    unique_lists = []
    for l in lists:
        l.sort()
        if l not in unique_lists:
            unique_lists.append(l)
    return unique_lists