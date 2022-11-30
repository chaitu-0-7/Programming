# Find out the maximum sub-array of non negative numbers from an array.

# The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

# Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

# Example:
# a = [1, 2, 5, -7, 2, 3]
# The two sub-arrays are[1, 2, 5][2, 3].
# The answer is [1, 2, 5] as its sum is larger than[2, 3]

# Input:
# n = 2
# a[] = {-1, 2}
# Output: 2
# Explanation: The only subarray[2] is
# the answer.


def findSubarray(a, n):
    start = 0
    end = 0
    temp_sum = 0
    res_sum = 0
    ans = []
    for i in range(n):
        if (a[i] >= 0):
            end = i
            temp_sum += a[i]
        else:
            if temp_sum > res_sum:
                res_sum = temp_sum
                ans = a[start:end+1]
            start = i+1
            temp_sum = 0
    if temp_sum > res_sum:
        ans = a[start:n+1]
    if len(ans) != 0:
        return ans
    return [-1]
print(findSubarray([1,2,3,-1,22],5))
