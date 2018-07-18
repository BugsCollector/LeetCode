import collections
from utils import *
class Solution(object):
    @get_run_time
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


o = Solution()
ret = o.twoSum([2, 7, 11, 15], 26)
print(ret)