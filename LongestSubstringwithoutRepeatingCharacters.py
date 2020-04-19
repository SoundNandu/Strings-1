Longest Substring Without Repeating Characters:
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Time : O(n)(basically its O(2n) each characters are visited 2 times) | Space : O(1) (In the set the max occupancy of elements will be 26 characters so the space is contant)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0:
            return 0
        start,end,maxLength = 0,0,0
        hashSet = set ()
        # start and end starts from the same position we need to check
        # end is less than len(s)
        while(end < len(s)):
            #ch contains the end value 
            ch = s[end]
            # we need to check whther the end value is present in set
            #if yes, we need remove from the set() and start ++
            #if no , we need to add into the set() end ++
            while(ch in hashSet):
                hashSet.remove(s[start])
                start += 1
            # compare the max value (previous maxLength, current window size)
            maxLength = max(maxLength, end - start + 1)
            hashSet.add(ch)
            end += 1
        return maxLength
