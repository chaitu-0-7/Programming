# Link to problem: https://leetcode.com/problems/non-decreasing-subsequences/

# 491. Non-decreasing Subsequences
# Given an integer array nums, return all the different possible non-decreasing subsequences 
# of the given array with at least two elements. You may return the answer in any order.

# Example 1:

# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

# Example 2:

# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def func(arr,ind,out,cur,prev):
            if ind==len(arr):
                if len(cur)>=2:
                    out.add(tuple(cur))
                return
            func(arr,ind+1,out,cur,prev)
            if arr[ind]>=prev:
                func(arr,ind+1,out,cur+[arr[ind]],arr[ind])
            # print(cur)
        out=set()
        func(nums,0,out,[],-101)
        return out