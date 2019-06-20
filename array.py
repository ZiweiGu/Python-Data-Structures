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


def plusOne(digits):
    carry = 1
    for i in reversed(range(len(digits))):
        if digits[i] == 9 and carry == 1:
            digits[i] = 0
            carry = 1
        else:
            digits[i] += carry
            carry = 0
    if carry == 1:
        return [1] + digits
    return digits


if __name__ == '__main__':
    print(plusOne([9, 9, 8]))
