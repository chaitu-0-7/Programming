# Link to Problem: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
# There is one meeting room in a firm. There are N meetings in the form of
#  (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
# What is the maximum number of meetings that can be accommodated in the
#  meeting room when only one meeting can be held in the meeting room at a particular time?

# Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


# Example 1:

# Input:
# N = 6
# start[] = {1,3,0,5,8,5}
# end[] =  {2,4,6,7,9,9}
# Output: 
# 4
# Explanation:
# Maximum four meetings can be held with
# given start and end timings.
# The meetings are - (1, 2),(3, 4), (5,7) and (8,9)
# Example 2:

# Input:
# N = 3
# start[] = {10, 12, 20}
# end[] = {20, 25, 30}
# Output: 
# 1
# Explanation:
# Only one meetings can be held
# with given start and end timings.

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        # if n==1:return 1
        t=[]
        for i in range(n):
            t.append([start[i],end[i]])
        t=sorted(t,key=lambda x:x[1])
        count=0
        prev=t[0]
        for i in range(n):
            if i==0 or t[i][0]>prev[1]:
                count+=1
                prev=t[i]
        return count