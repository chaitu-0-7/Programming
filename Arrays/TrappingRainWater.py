# Link to Problem: https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Refer Problem link for clear explination

class Solution:
    def trap(self, arr: List[int]) -> int:
        if len(arr)<=2:return 0
        l=arr.copy()
        for i in range(1,len(arr)):
            l[i]=max(l[i],l[i-1])
        r=arr.copy()
        for i in range(len(arr)-2,-1,-1):
            r[i]=max(r[i],r[i+1])
        # print(l,r)
        ans=0
        for i in range(1,len(arr)-1):
            t=(min(l[i-1],r[i+1])-arr[i])
            if t>0:
                ans+=t
        return ans
