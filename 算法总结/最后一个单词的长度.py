'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

'''
#  库函数方法  split
def lengthOfLastWord(self, s: str) -> int:
    s = s.split()
    if not s : return 0
    return len(s[-1])



'''
直接找最后一个单词

先找最后一个单词最后一个字母

再找最后一个单词第一个字母
'''
def lengthOfLastWord(self, s: str) -> int:
    end = len(s) - 1
    while end >= 0 and s[end] == " ":
        end -= 1
    if end == -1: return 0
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
    return end - start
