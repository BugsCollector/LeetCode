class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        startRepeat = False
        longest_str = ""
        ret = ""
        retro_index = -1
        for i in range(0, len(s)):
            startRepeat = False
            longest_str = ""
            mirror_index = -1
            retro_index = -1
            for j in range(i, len(s)):
                if s[j] not in longest_str:
                    if not startRepeat:
                        longest_str += s[j]
                    else:
                        break
                else:
                    # s[j] already in the longest_str
                    if not startRepeat:
                        startRepeat = True
                        longest_str += s[j]
                        retro_index = longest_str.find(s[j])

                    if retro_index >= 0 and s[j] == longest_str[retro_index]:
                        if retro_index > 0:
                            retro_index -= 1
                        elif len(longest_str) >= len(ret):
                            ret = longest_str
                            break
        return ret


obj = Solution()
print("input: babad")
print(obj.longestPalindrome("babad"))
print("input: cbbd")
print(obj.longestPalindrome("cbbd"))