"""
三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/75/

"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        三个数：中间数字固定去找两边的
        排序nlogn，找数字n*n
        这个版本各种超时，用C++版本完全没问题，实在是= = 
        
        """

        nums.sort()
        print(nums)
        result = []
        for index in range(len(nums)-2):
            i = index + 1
            j = len(nums)-1  # 双指针
            indexnum = nums[index]  # 数字大小
            if index > 0 and nums[index] == nums[index-1]:
                continue
            while i < j:
                if nums[i] + nums[j] + indexnum > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif nums[i] + nums[j] < -indexnum:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                else:
                    tmp = [indexnum, nums[i], nums[j]]
                    # if tmp not in result:
                    result.append(tmp)
                    i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
        return result
        
