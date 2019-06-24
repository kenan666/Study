'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。  **

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

'''
def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1,-1]
    
    res = [-1,-1]
    left = 0
    n = len(nums)
    right = n-1

    while left < right:
        mid = left + (right - left) // 2 
        if nums[mid] == target:
            left = mid
            right = mid 
            while left >0 and nums[left - 1] == nums[right]:
                left -= 1
            while right < n - 1 and nums[right] == nums[right+1]:
                right += 1
            
            res[0] = left
            res[1] = right
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return res


'''
思路1 版本 2
'''
def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1,-1]
    
    res = [-1,-1]
    left = 0
    n = len(nums)
    right = n-1

    while left < right:
        mid = left +(right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid 
    
    res[0] = left if left < n and nums[left] == target else -1
    if res[0] == -1:
        return res
    while left < n-1 and nums[left] == nums[left + 1]:
        left += 1 
    return res



'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

'''
#  思路  二分法
def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2 
            if nums[mid] == target:return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left