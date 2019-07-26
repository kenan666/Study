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

'''
1、旋转排序数组nums可以被拆分为2个排序数组nums1, nums2，并且nums1所有元素>=nums2所有元素；因此，考虑二分法寻找值nums[i]；

2、设置left, right指针在nums数组两端，mid为中点：

    ·当nums[mid] > nums[right]时，一定满足mid < i <= right，因此left = mid + 1；
    ·当nums[mid] < nums[right]时，一定满足left < i <= mid，因此right = mid；
    ·当nums[mid] == nums[right]时，是此题对比153题的难点（原因是此题中数组的元素可重复，相等就难以判断最小值的指针区间）；先说结果：采用right = right - 1，

        下面证明：
        ·首先，此操作不会使数组越界，因为right > left > 0；
        ·其次，此操作不会使最小值丢失，证明：假设'nums[right]'是最小值，有两种情况：

            ·若nums[right]是唯一最小值：那就不可能满足判断条件nums[mid] == nums[right]，因为left != right且mid = left + right // 2 < right（向下取整）；
            ·若有其他元素和nums[right]同为最小值：还有最小值存在于[left, right -1]间，不会丢失最小值。

以上是理论分析，可以用以下数组辅助思考：
[1, 2, 3]
[1, 1, 0, 1]
[1, 0, 1, 1, 1]
[1, 1, 1, 1]

'''
def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]: 
            left = mid + 1
        elif nums[mid] < nums[right]: 
            right = mid
        else: 
            right = right - 1 # key
    return nums[left]