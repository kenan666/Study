'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

'''
'''
第一常规解题思路  

栈

对于这种括号匹配问题，一般都是使用栈

我们先找到所有可以匹配的索引号，然后找出最长连续数列！

例如：s = )(()())，我们用栈可以找到，

位置 2 和位置 3 匹配，

位置 4 和位置 5 匹配，

位置 1 和位置 6 匹配，

这个数组为：2,3,4,5,1,6 这是通过栈找到的,我们按递增排序！1,2,3,4,5,6

找出该数组的最长连续数列的长度就是最长有效括号长度！

所以时间复杂度来自排序：O(nlogn)

接下来我们思考，是否可以省略排序的过程,在弹栈时候进行操作呢?

直接看代码理解!所以时间复杂度为：O(n)

'''
def longestValidParentheses(self, s: str) -> int:
    if not s:
        return 0
    
    res = []
    stack = []
    for i in range (len(s)):
        if stack and s[i] == ")":
            res.append(stack.pop())
            res.append(i)
        if s[i] == "(":
            stack.append(i)

    res.sort()

    i = 0
    ans = 0
    n = len(res)
    while i<n:
        j = i 
        while j < n-1 and res[j+1] = res[j] + 1:
            j += 1
        ans = max(ans,j-i+1)
        i = j+1
    return ans 

#   解  2
def longestValidParentheses(self, s: str) -> int:
    if not s :
        return 0

    res = 0
    stack = [-1]

    for i in range (len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res,i - stack[-1])

    return res
