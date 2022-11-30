# Given an integer array nums, find the 
# subarray
#  which has the largest sum and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23



def maxSubArray(nums):
        ans=-1000000
        temp=0
        for i in range(len(nums)):
            temp+=nums[i]
            ans=max(ans,temp)
            if(temp<0):
                temp=0
        return ans