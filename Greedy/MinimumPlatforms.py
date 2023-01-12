# Link to Problem: https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

# Given arrival and departure times of all trains that reach a railway station. 
# Find the minimum number of platforms required for the railway station so that no train is kept waiting.
# Consider that all the trains arrive on the same day and leave on the same day.
#  Arrival and departure time can never be the same for a train but we can have arrival
#   time of one train equal to departure time of the other. At any given instance of time, 
#   same platform can not be used for both departure of a train and arrival of another train.
#    In such cases, we need different platforms.


# Example 1:

# Input: n = 6 
# arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
# dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
# Output: 3
# Explanation: 
# Minimum 3 platforms are required to 
# safely arrive and depart all trains.
# Example 2:

# Input: n = 3
# arr[] = {0900, 1100, 1235}
# dep[] = {1000, 1200, 1240}
# Output: 1
# Explanation: Only 1 platform is required to 
# safely manage the arrival and departure 
# of all trains. 

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        ans=0
        plat=1
        i=1
        j=0
        while(i<n and j<n):
            if arr[i]<=dep[j]:
                plat+=1
                i+=1
            else:
                plat-=1
                j+=1
            ans=max(ans,plat)
        return ans
