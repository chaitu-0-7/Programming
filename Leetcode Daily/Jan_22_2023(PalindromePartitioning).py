# Link to problem: https://leetcode.com/problems/palindrome-partitioning/description/

# Given a string s, partition s such that every 
# substring of the partition is a 
# palindrome
# Return all possible palindrome partitioning of s.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:

# Input: s = "a"
# Output: [["a"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
    
        def backtrack(s, ans, candidates, start):
            if start == len(s):
                ans.append(list(candidates))
                return
            for i in range(start, len(s)):
                candidate = s[start:i+1]
                if not is_palindrome(candidate):
                    continue
                candidates.append(candidate)
                backtrack(s, ans, candidates, i + 1)
                candidates.pop()
        ans = []
        candidates = []
        backtrack(s, ans, candidates, 0)
        return ans