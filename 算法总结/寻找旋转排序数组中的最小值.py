'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:
输入: [3,4,5,1,2]
输出: 1

示例 2:
输入: [4,5,6,7,0,1,2]
输出: 0

'''
'''
1、nums[mid] > nums[right]：例子：[7, 8, 9, 10, 1, 2]，mid 肯定不是最小；

2、否则，nums[mid] < nums[right]：例子：[8, 9, 1, 2, 3, 4, 5, 6]，此时 mid 有可能是最小。

'''
def findMin(self, nums: List[int]) -> int:
    size = len(nums)
    if size == 0:
        raise Exception('程序出错')
    if size == 1:
        return nums[0]
    left = 0
    right = size - 1
    while left < right:
        mid = (left + right) >> 1
        # [7, 8, 1, 2, 3, 4, 5, 6]
        if nums[mid] > nums[right]:
            # [3, 4, 5, 6, 7, 8, 1, 2]
            # 此时 mid 肯定不是最小元素
            left = mid + 1
        else:
            # mid 有可能是最小元素，所以，不能排除它
            assert nums[mid] < nums[right]
            right = mid
    # 一定存在最小元素，因此无需再做判断
    return nums[left]


'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：
输入: [1,3,5]
输出: 1

示例 2：
输入: [2,2,2,0,1]
输出: 0

'''
