# Link to Problem: https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
#  i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        out=[]
        for i in range(len(arr)-2):
            if i==0 or arr[i]!=arr[i-1]:
                lo=i+1
                hi=len(arr)-1
                suma=0-arr[i]
                while(lo<hi):
                    if arr[lo]+arr[hi]==suma:
                        out.append([arr[i],arr[lo],arr[hi]])
                        while(lo<hi and arr[lo]==arr[lo+1]):lo+=1
                        while(hi>lo and arr[hi]==arr[hi-1]):hi-=1
                        lo+=1
                        hi-=1
                    elif(arr[lo]+arr[hi]>suma):
                        hi-=1
                    else:lo+=1
        return out