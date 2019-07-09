'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

'''
# 思路一: 统计每种颜色的个数,重新覆盖原数组
def sortColors(self, nums: List[int]) -> None:
    from collections import Counter
    c_nums = Counter(nums)
    p = 0
    for i in range(3):
        for _ in range(c_nums[i]):
            nums[p] = i
            p += 1


# 思路二:因为0和2分别在排序之后一定在最左边,和最右边,所以我们用双指针分别记录最左边,和最右边,依次把0,2交换过去!

def sortColors(self, nums: List[int]) -> None:

    left = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
    #print(nums)
    right = len(nums) - 1
    for i in range(len(nums) - 1, left - 1, -1):
        if nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1

def sortColors(self, nums: List[int]) -> None:
    
    left = 0
    right = len(nums) - 1
    i  = 0
    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1
