'''
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

例如:
输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）： 

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

'''
#--思路--参考解析--中位数思想---
'''
假如数组长度为奇数2n+1 则中位数两边各有n个数 

设左边所有数和中位数的差值和为x 右边所有数和中位数的差值和为y 则所有需要移动的次数为x+y 

如果不选择中位数 例如选择中位数-1 这样总的移动次数就变成了 >= ((x-n) + (y+n) + 1) 最好的情况下比中位数大1 

如果数组长度是偶数 有两个中位数 选择两个中位数的任何一个或者两个中位数的平均数 都是可以的
'''
def minMoves2(nums):
    nums = sorted(nums)
    m = nums[len(nums)//2]
    ans = 0
    for num in nums:
        ans += abs(num-m)
    return ans

