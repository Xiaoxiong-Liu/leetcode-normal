”“”
字谜分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/77/

“”“
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for x in strs:
            key = tuple(sorted(x))
            d[key] = d.get(key,[]) + [x]
        return list(d.values())
