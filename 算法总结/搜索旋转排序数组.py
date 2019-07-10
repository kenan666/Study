'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

'''
'''
 二分法,判断二分点,几种可能性

直接nums[mid] == target

当数组为[1,2,1,1,1],nums[mid] == nums[left] == nums[right],需要left++, right --;

当nums[left]<= nums[mid],说明是在左半边的递增区域

​	a. nums[left] <=target < nums[mid],说明target在left和mid之间.我们令right = mid - 1;

​	b. 不在之间, 我们令 left = mid + 1;

当nums[mid] < nums[right],说明是在右半边的递增区域

​	a. nums[mid] < target <= nums[right],说明target在mid 和right之间,我们令left = mid + 1

​	b. 不在之间,我们令right = mid - 1;

时间复杂度:O(logn)O(logn)

'''
def search(self, nums: List[int], target: int) -> bool:
        
    left = 0
    right = len(nums) - 1
    while left <= right:
        #print(left, right)
        mid = left + (right - left) // 2
        # 等于目标值
        if nums[mid] == target:return True
        
        if nums[mid] == nums[left] == nums[right]:
            left += 1
            right -= 1
        # 在前部分
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False
