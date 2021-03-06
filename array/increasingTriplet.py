"""
递增的三元子序列
给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

数学表达式如下:

如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。

示例 1:

输入: [1,2,3,4,5]
输出: true
示例 2:

输入: [5,4,3,2,1]
输出: false

https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/80/

"""
import sys
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
#         # 简单的n2解法
#         for i in range(1,len(nums)-1):
#             left = False
#             right = False
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     left = True
#                     break
#             for k in range(i+1,len(nums)):
#                 if nums[i] < nums[k]:
#                     right = True
#             if left and right:
#                 return True
#         return False

        n1 = sys.maxsize
        n2 = sys.maxsize
        for i in nums:
            if i <= n1:
                n1 = i
            elif i <= n2:
                n2 = i
            else:
                return True
        return False
