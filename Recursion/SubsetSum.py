# Link to Problem: https://practice.geeksforgeeks.org/problems/subset-sums2234/1

# Given a list arr of N integers, print sums of all subsets in it.

# Example 1:

# Input:
# N = 2
# arr[] = {2, 3}
# Output:
# 0 2 3 5
# Explanation:
# When no elements is taken then Sum = 0.
# When only 2 is taken then Sum = 2.
# When only 3 is taken then Sum = 3.
# When element 2 and 3 are taken then 
# Sum = 2+3 = 5.
# Example 2:

# Input:
# N = 3
# arr = {5, 2, 1}
# Output:
# 0 1 2 3 5 6 7 8

class Solution:
	def subsetSums(self, arr, N):
		def func(ind,n,arr,out,cursum):
		    if ind==n:
		        out.append(cursum)
		        return
		    func(ind+1,n,arr,out,cursum+arr[ind])
		    func(ind+1,n,arr,out,cursum)
		    return
		out=[]
		func(0,N,arr,out,0)
		return sorted(out)