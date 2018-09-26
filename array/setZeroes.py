"""
矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/76/

最优解：
按从左到右从上到下的顺序找到原始数据中第一个0元素（其实可以是任意一个0元素），假设为X[row][col]，则用X中的第row行和第col列空间来作为标记空间。其中第row行用来标记某一列是否需要置零，第col列用来标记某一行是否需要置零
遍历原始数据，如果某一元素为X[i][j]=0，则修改X[row][j]和X[i][col]
根据第row行和第col列，对X中的元素进行置零
其实就是没有单独开辟空间而是将矩阵本身拿来用。想法巧妙。

"""

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            matrix[i] = [0]*len(matrix[0])
        col = list(col)
        for j in  col:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        
# 2018.09.26 没有做实现。 TODO
