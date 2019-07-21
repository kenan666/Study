'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

'''
# 回溯法
def partition(self, s: str) -> List[List[str]]:
    res = []
    
    def helper(s, tmp):
        if not s:
            res.append(tmp)
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                helper(s[i:], tmp + [s[:i]])
    helper(s, [])
    return res


# 动态规划 + DFS
# 用 dp[j][i] 字符串从位置 j 到位置 i(闭区间)是否为回文子串
# 再用 DFS 把所有可能找到
def partition(self, s: str) -> List[List[str]]:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                dp[j][i] = True
    #print(dp)
    res = []
    def helper(i, tmp):
        if i == n:
            res.append(tmp)
        for j in range(i, n):
            if dp[i][j]:
                helper(j + 1, tmp + [s[i: j + 1]])
    helper(0, [])
    return res
