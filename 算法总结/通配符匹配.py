'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false

'''
#  双指针遍历
def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    i = 0
    j = 0
    start = -1
    match = 0
    while i < len(s):
        #一对一匹配，匹配成功一起移动
        if j <len(p) and (s[i] == p[j] or p[j] == "?"):
            i += 1
            j += 1
        
        # 记录p的 * 位置，还有 s 的位置
        elif j < len(p) and p[j] == "*":
            start = j
            match = i
            j += 1

        # j 回到 记录的下一个位置
        # match 更新下一个位置
        # 这不代表用*匹配一个字符
        elif start != -1:
            j = start + 1
            match += 1
            i = match

        else:
            return False
    
    # 将多余的 * 直接匹配空串
    return all (x == "*" for x in p[j:])