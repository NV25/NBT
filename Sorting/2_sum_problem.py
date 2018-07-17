#########################################
#######     Given an array, return indices of 2 numbers that add to target
#######     Time: O(n) Space: O(n)
#########################################

def TwoSum(nums, target):
    res = []
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen.keys():
            res = [i, seen[nums[i]]]
            break
        else:
            diff = target - nums[i]
            seen[diff] = i
    return res


#########################################
#######     Given a sorted array, return 2 numbers that add to target
#######     Time: O(n) Space: O(1)
#######     Time: O(nlogn+n) Space: O(1) ===> If array is unsorted
#########################################

def TwoSum(nums, target):
    res = []
    #nums.sort()

    i = 0
    j = len(nums) - 1

    while (i <= j):
        cur_sum = nums[i] + nums[j]
        if cur_sum == target:
            res = [nums[i], nums[j]]
            break
        elif cur_sum < target:
            i = i + 1
        elif cur_sum > target:
            j = j - 1
    return res


#########################################
#######     Given a sorted  array, return all sets of 2 numbers that add to target
#######     Time: O(n) Space: O(1)
#########################################
def TwoSum(nums, target):
    res = []
    i = 0
    j = len(nums) - 1

    while(i<=j):
        cur_sum = nums[i] + nums[j]
        if cur_sum == target:
            res.append(nums[i], nums[j])
        elif cur_sum < target:
            i = i + 1
        else:
            j = j - 1

    return res

