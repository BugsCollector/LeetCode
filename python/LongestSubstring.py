"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        mapping = [0 for i in range(0,26)]
        to_be_processed = s.lower()
        temp_longest = 0
        startPos = 0
        endPos = 0
        for start in range(0, len(to_be_processed) - 1):
            print('Read start word: {0}'.format(to_be_processed[start]))
            for end in range(start, len(to_be_processed)):
                print('Read end word: {0}'.format(to_be_processed[end]))
                if mapping[ord(to_be_processed[end]) - ord('a')] == 0:
                    temp_longest += 1
                    mapping[ord(to_be_processed[end]) - ord('a')] = 1
                else:
                    if temp_longest > longest:
                        longest = temp_longest
                        startPos = start
                        endPos = end
                        print('Update longest substring: {0}'.format(s[startPos: endPos]))
                    mapping = [0 for i in range(0, 26)]
                    temp_longest = 0
                    break
        return longest, s[startPos: endPos]

obj = Solution()
s = 'pwwkew'
len, substr = obj.lengthOfLongestSubstring(s)
print(len)
print(substr)