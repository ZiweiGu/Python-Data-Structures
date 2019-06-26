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


def maxProfit(prices):
    if len(prices) < 2:
        return 0
    start = prices[0]
    profit = []
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:
            profit.append(max(0, prices[i-1] - start))
            start = prices[i]
    if prices[-1] >= prices[-2]:
        profit.append(prices[-1] - start)
    if len(profit) == 0:
        return 0
    if len(profit) == 1:
        return profit[0]
    profit.sort()
    return profit[-1] + profit[-2]


if __name__ == '__main__':
    print(maxProfit([7, 6, 4, 3, 1]))
