'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

'''

#  二分法
'''
直接使用二分法，判断那个二分点,有几种可能性

直接等于target

在左半边的递增区域

a. target 在 left 和 mid 之间

b. 不在之间

在右半边的递增区域

a. target 在 mid 和 right 之间

b. 不在之间

'''
 def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return -1
    left = 0
    right = n - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
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
    #print(left,right)
    return left if nums[left] == target else -1



#**********************************************
'''
二分法

'''
int bsearch(int array[], int low, int high, int target)
{
    if (low > high) return -1;
    
    int mid = (low + high)/2;
    if (array[mid]> target)
        return    binarysearch(array, low, mid -1, target);
    if (array[mid]< target)
        return    binarysearch(array, mid+1, high, target);
    
    //if (midValue == target)
        return mid;
}