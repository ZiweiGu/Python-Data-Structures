"""
Data Structure 1: Array
"""
import sys


def search_insert_pos(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            if mid == len(nums) - 1:
                return mid + 1
            if target < nums[mid+1]:
                return mid + 1
            l = mid + 1
        else:
            if mid == 0:
                return 0
            if target > nums[mid-1]:
                return mid
            r = mid - 1
    return 0


# Better time
def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


def maxSubArray(nums):
    max_sum = nums[0]
    buff = nums[0]
    for i in range(1, len(nums)):
        buff += nums[i]
        if nums[i] > buff and buff > 0:
            max_sum = nums[i]
            buff = nums[i]
        else:
            max_sum = max(buff, max_sum)
    return max_sum


if __name__ == '__main__':
    print(maxSubArray([-2, -1]))
