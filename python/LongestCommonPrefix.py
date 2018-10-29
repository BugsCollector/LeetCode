"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest = {}
        length = 0
        ret = ""
        for s in strs:
            if len(s) >= length:
                shortest.update({s, len(s)})

        for item in shortest:
            s = item[0]
            length = item[1]
            for prefixLen in range(0, length):
                commonPrefix = s[:prefixLen]
                for tmp in strs:
                    myPrefix = tmp[:prefixLen]
                    if myPrefix != commonPrefix:
                        break
                if len(commonPrefix) >= len(ret):
                    ret = commonPrefix

        return ret