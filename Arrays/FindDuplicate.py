# Link to Problem: https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        n=len(arr)
        for i in range(n):
            arr[(arr[i]-1)%(n+1)]+=n+1
        for i in range(n):
            if arr[i]//(n+1)>=2:ans=i+1
            arr[i]=arr[i]%(n+1)
        return ans