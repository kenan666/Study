'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

************题目难度：难**************
'''

'''
思路：
先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
再找出另一个最大索引 l 满足 nums[l] > nums[k]；
交换 nums[l] 和 nums[k]；
最后翻转 nums[k+1:]

'''

'''
例子：
比如 nums = [1,2,7,4,3,1]，下一个排列是什么？

我们找到第一个最大索引是 nums[1] = 2

再找到第二个最大索引是 nums[5] = 3

交换，nums = [1,3,7,4,2,1];

翻转，nums = [1,3,1,2,4,7]

结束！！！
'''
def nextPermutation(self, nums: List[int]) -> None:
    firstIndex = -1
    n = len(nums)
    def reverse(nums,i,j):
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
    
    for i in range (n-2,-1,-1):
        if nums[i]<nums[i+1]:
            firstIndex = i
            break

    if firstIndex == -1 :
        reverse(nums,0,n-1)
        return

    secondIndex = -1
    for i in range (n-1,firstIndex,-1):
        if nums[i] > num[firstIndex]:
            secondIndex = i
            break
        
    nums[firstIndex],nums[secondIndex] = nums[secondIndex],nums[firstIndex]
    reverse(nums,firstIndex+1,n-1)