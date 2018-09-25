"""
最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/79/

"""

def longestPalindrome(self, s1):
        """
        :type s: str
        :rtype: str
        """
        #预处理
        s='#'+'#'.join(s1)+'#'

        RL=[0]*len(s)
        MaxRight=0
        pos=0
        MaxLen=0
        maxPos = 0
        for i in range(len(s)):
            if i<MaxRight:
                RL[i]=min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i]=1
            #尝试扩展，注意处理边界
            while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
                RL[i]+=1
            #更新MaxRight,pos
            if RL[i]+i-1>MaxRight:
                MaxRight=RL[i]+i-1
                pos=i
                print("pos:",str(pos))
            #更新最长回文串的长度
            if MaxLen < RL[i]:
                
                maxPos = i
                MaxLen=RL[i]
                print("MaxLen:",str(MaxLen))
                print("i:",str(i))
        
        # print(s)
        # print(MaxLen-1)
        # print(pos)
        # print(maxPos)
        MaxLen = MaxLen - 1
        result =  s[maxPos-MaxLen:maxPos+MaxLen]
        # print(result)
        ll = result.split("#")
        # print("".join(ll))
        return "".join(ll)
