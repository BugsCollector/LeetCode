"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        translationMap = {
            'M':    1000,
            'CM':   900,
            'D':    500,
            'CD':   400,
            'C':    100,
            'XC':   90,
            'L':    50,
            'XL':   40,
            'X':    10,
            'IX':   9,
            'V':    5,
            'IV':   4,
            'I':    1
        }
        ret = 0
        length = len(s)
        pos = 0
        while pos < length:
            combined = False
            ch = s[pos]
            if pos != length - 1:
                ch += s[pos + 1]
                combined = True
            if ch in translationMap.keys():
                ret += translationMap[ch]
                if combined:
                    pos += 1
            elif combined:
                ret += translationMap[s[pos]]
            pos += 1


        return ret


obj = Solution()
testCases = {"I":       1,
             "III":     3,
             "IV":      4,
             "IX":      9,
             "XII":     12,
             "XX":      20,
             "XLII":    42,
             "LVIII":   58,
             "XCIV":    94,
             "CXXIII":  123,
             "CDXXI":   421,
             "MCMXCIV": 1994
             }
for test, result in testCases.iteritems():
    print("Testing {0}...".format(test))
    ret = obj.romanToInt(test)
    print("{0}: expected:{1}, real:{2}".format(test, result, ret))
