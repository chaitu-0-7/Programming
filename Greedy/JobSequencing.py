# Link to Problem: https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

# Given a set of N jobs where each jobi has a deadline and profit associated with it.

# Each job takes 1 unit of time to complete and only one job can be scheduled at a time. 
# We earn the profit associated with job if and only if the job is completed by its deadline.

# Find the number of jobs done and the maximum profit.

# Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.


# Example 1:

# Input:
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output:
# 2 60
# Explanation:
# Job1 and Job3 can be done with
# maximum profit of 60 (20+40).
# Example 2:

# Input:
# N = 5
# Jobs = {(1,2,100),(2,1,19),(3,2,27),
#         (4,1,25),(5,1,15)}
# Output:
# 2 127
# Explanation:
# 2 jobs can be done with
# maximum profit of 127 (100+27).

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        t=[]
        maxi=-1
        for i in Jobs:
            t.append([i.id,i.deadline,i.profit])
            maxi=max(i.deadline,maxi)
        Jobs=sorted(t,key=lambda x:x[2])
        visited=[False for i in range(maxi+1)]
        count=0
        pro=0
        for i in range(n-1,-1,-1):
            if visited[Jobs[i][1]-1]==False:
                visited[Jobs[i][1]-1]=True
                count+=1
                pro+=Jobs[i][2]
            else:
                for j in range(Jobs[i][1]-1,-1,-1):
                    if visited[j]==False:
                        visited[j]=True
                        count+=1
                        pro+=Jobs[i][2]
                        break
        return count,pro