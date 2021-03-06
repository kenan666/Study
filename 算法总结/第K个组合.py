'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

'''
'''
找规律：
n = 3, k = 3

num = [1, 2, 3]这三个数组成
所有数;

"123"
"132"
"213"
"231"
"312"
"321"

当首数字确定了,后面和首数字组成数字的个数相等的!

比如: 首数字为1,后面有组成两个数123,132,可以组成2个数.当首数字为2,3同样都是.

所有我们要找k = 3的数字 ,我们只需要 3/2 便可找到首数字什么,

'''

def getPermutation(self, n: int, k: int) -> str:
    num = [str(i) for i in range(1, n+1)]
    res = ""
    n -= 1
    while n > -1:
        t = math.factorial(n)
        loc = math.ceil(k / t) - 1
        res += num[loc]
        num.pop(loc)
        k %= t
        n -= 1
    return res
