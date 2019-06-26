'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

'''
'''
我们先来简单回顾一下小学老师教过的列竖式求乘法的过程：

如下图所示，两个数M和N相乘的结果可以由 M 乘上 N 的每一位数的和得到。

举例 123 * 45 = 123 * 5 + 123 *40 = 615 + 4920 = 5535

'''
#  本题 第一步
'''
字符串的乘法也可以由列竖式计算的方法得到：

让num1 依次乘上 num2 的每一位的和
把第一步里得到的所有和累加在一起，就可以得到 num1 * num2 的结果。

'''
def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if num1 == "0" or num2 == "0": #处理特殊情况
        return "0"
    
    l1, l2 = len(num1), len(num2) 
    if l1 < l2: 
        num1, num2 = num2, num1 #保障num1始终比num2长， 
        l1, l2 = l2, l1
        
    num2 = num2[::-1] #注意要倒过来乘，方便进位
    res = "0"
    for i, digit in enumerate(num2):
        tmp = self.StringMultiplyDigit(num1, int(digit)) + "0" * i #计算num1和num2的当前位的乘积
        res = self.StringPlusString(res, tmp) #计算res和tmp的和

    return res

# 第二步
'''
开一个数组 res, res[i] = int(string[i]) * n
乘完之后再调用第二个辅助函数处理 res 里的进位
最后把 res 转成字符串返回

第二个函数为了处理乘法结果里的进位：

思路：

把每一位上超过 10 的部分都向后进位，

注意处理最后一位进位时数组需要 append 一下，否则会 下标越界 。

'''
def StringMultiplyDigit(self,string, n):
    #这个函数的功能是：计算一个字符串和一个整数的乘积，返回字符串
    #举例：输入为 "123", 3， 返回"369"
    s = string[::-1]
    res = []
    for i, char in enumerate(s):
        num = int(char)
        res.append(num * n)
    res = self.CarrySolver(res)
    res = res[::-1]
    return "".join(str(x) for x in res)


# 第三步
def CarrySolver(self, nums):  
    #这个函数的功能是：将输入的数组中的每一位处理好进位
    #举例：输入[15, 27, 12], 返回[5, 8, 4, 1]
    i = 0
    while i < len(nums):
        if nums[i] >= 10:
            carrier = nums[i] // 10
            if i == len(nums) - 1:
                nums.append(carrier)
            else:
                nums[i + 1] += carrier
            nums[i] %= 10
        i += 1


#  代码整合
def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if num1 == "0" or num2 == "0": #处理特殊情况
        return "0"
    
    l1, l2 = len(num1), len(num2) 
    if l1 < l2: 
        num1, num2 = num2, num1 #保障num1始终比num2大
        l1, l2 = l2, l1
        
    num2 = num2[::-1]
    res = "0"
    for i, digit in enumerate(num2):
        tmp = self.StringMultiplyDigit(num1, int(digit)) + "0" * i #计算num1和num2的当前位的乘积
        res = self.StringPlusString(res, tmp) #计算res和tmp的和

    return res

def StringMultiplyDigit(self,string, n):
    #这个函数的功能是：计算一个字符串和一个整数的乘积，返回字符串
    #举例：输入为 "123", 3， 返回"369"
    s = string[::-1]
    res = []
    for i, char in enumerate(s):
        num = int(char)
        res.append(num * n)
    res = self.CarrySolver(res)
    res = res[::-1]
    return "".join(str(x) for x in res)
    
def CarrySolver(self, nums):  
    #这个函数的功能是：将输入的数组中的每一位处理好进位
    #举例：输入[15, 27, 12], 返回[5, 8, 4, 1]
    i = 0
    while i < len(nums):
        if nums[i] >= 10:
            carrier = nums[i] // 10
            if i == len(nums) - 1:
                nums.append(carrier)
            else:
                nums[i + 1] += carrier
            nums[i] %= 10
        i += 1
                
    return nums
    
def StringPlusString(self, s1, s2):
    #这个函数的功能是：计算两个字符串的和。 
    #举例：输入为“123”， “456”, 返回为"579"
    #PS：LeetCode415题就是要写这个函数
    l1, l2 = len(s1), len(s2)
    if l1 < l2:
        s1, s2 = s2, s1
        l1, l2 = l2, l1
    s1 = [int(x) for x in s1]
    s2 = [int(x) for x in s2]
    s1, s2 = s1[::-1], s2[::-1]
    for i, digit in enumerate(s2):
        s1[i] += s2[i]
        
    s1 = self.CarrySolver(s1)
    s1 = s1[::-1]
    return "".join(str(x) for x in s1)
