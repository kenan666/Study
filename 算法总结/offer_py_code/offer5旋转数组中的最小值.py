'''
题目：

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

'''
'''
思路：
使用二分法，但要考虑[1, 0, 0, 1]这种数据，只能顺序查找
'''
def findMin(nums):
    if not nums :
        return False
    
    length = len(nums)
    left = 0
    right = length -1

    while nums[left] >= nums[right]:
        if right - left == 1:
            return nums[right]

        mid = (left + right) / 2
        if nums[left] == nums[mid] == nums[right]:
            return min(nums)

        if nums[left] <= nums[mid]:
            left = mid 

        if nums[right] >= nums[mid]:
            right = mid 
    
    return nums[0]

nums = [3,4,5,6,1,2]
findMin(nums)