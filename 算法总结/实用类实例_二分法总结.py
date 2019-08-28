# ------------关于二分法的总结-------------

# 1、--------什么是二分查找------------
'''
二分查找是计算机科学中最基本、最有用的算法之一。 它描述了在有序集合中搜索特定值的过程。

二分查找中使用的术语：

    ·目标 Target —— 你要查找的值
    ·索引 Index —— 你要查找的当前位置
    ·左、右指示符 Left，Right —— 我们用来维持查找空间的指标
    ·中间指示符 Mid —— 我们用来应用条件来确定我们应该向左查找还是向右查找的索引

'''

# 2、------ 简单例子 ---------------
'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。

'''
#-------------解--------------->
def getTarget(nums,target):
    
    if len(nums) == 0:
        return False
    
    left ,right = 0,len(nums)-1
    while left < right:
        mid = (left + right) //2
        if nums[mid] > target:
            right = nums[mid] - 1
        elif nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            left = nums[mid] + 1
    return -1

# 3、----------识别和模板-------------
'''
1、如何识别而分查找？

二分查找是一种在每次比较之后将查找空间一分为二的算法。每次需要查找集合中的索引或元素时，都应该考虑二分查找。
*如果集合是无序的，我们可以总是在应用二分查找之前先对其进行排序。
         -------                     ---------------------

    * 成功的二分查找分为3各部分
    1、预处理--如果集合未排序，则进行排序
    2、二分查找--使用循环或者递归在每次比较后将查找空间划分为两半
    3、后处理--在剩余空间中确定可行的候选者

'''

# 4、--------二分查找模板1-------------
'''
模板 #1 是二分查找的最基础和最基本的形式。这是一个标准的二分查找模板。
模板 #1 用于查找可以通过访问数组中的单个索引来确定的元素或条件。
'''

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

#---关键属性----
'''
· 二分查找的最基础和最基本的形式。
· 查找条件可以在不与元素的两侧进行比较的情况下确定（或使用它周围的特定元素）。
· 不需要后处理，因为每一步中，你都在检查是否找到了元素。如果到达末尾，则知道未找到该元素。
'''
# ----区分语法---
'''
· 初始条件：left = 0, right = length-1
· 终止：left > right
· 向左查找：right = mid-1
· 向右查找：left = mid+1
'''
#------例1 --->   x的平方根  <--------
'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2

说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
'''
#------->  >>  解 1  ------
import math
def mySqrt(x):
    if x <= 0:
        return False
    while x > 0:
        left = 0
        right = math.ceil(x/2)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            tmp = mid * mid
            if tmp == x:
                return mid 
            elif tmp < x:
                left = mid + 1
            else :
                right = mid -1 
                #print(right)
    return right

#---例2--->   猜数字大小  <--------
'''
我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！

示例 :

输入: n = 10, pick = 6
输出: 6

def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
'''
#-------------解 1---------------
def guessNumber(n,target):
    if not n:
        return False
    while n:
        left = 1
        right = n
        mid = (left + right) //2
        
        if mid == target:
            return 0
        elif mid < target:
            left = mid + 1
            return -1
        else :
            right = mid -1 
            return 1

#---例3--->   搜索旋转排序数组  <--------
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
'''
#-------------解1----------------
def getTarget(nums,target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        #print(mid)
        
        if nums[mid] == target:
            return mid
        if nums[mid] == nums[left] == nums[right]:
            left += 1
            right -= 1
        
        elif nums[left] <= nums[mid]:  #  下面进行 target 与左右两边值的判断，由此来判断 mid 的位置
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

#-----模板2---------
'''
模板 #2 是二分查找的高级模板。它用于查找需要访问数组中当前索引及其直接右邻居索引的元素或条件。
'''
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1

#----关键属性-----
'''
·  一种实现二分查找的高级方法。
·  查找条件需要访问元素的直接右邻居。
·  使用元素的右邻居来确定是否满足条件，并决定是向左还是向右。
·  保证查找空间在每一步中至少有 2 个元素。
·  需要进行后处理。 当你剩下 1 个元素时，循环 / 递归结束。 需要评估剩余元素是否符合条件。

'''

#----区分语法---------
'''
·  初始条件：left = 0, right = length
·  终止：left == right
·  向左查找：right = mid
·  向右查找：left = mid+1
'''

##------例1--->   第一个版本的错误  <--------
'''
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。
由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。
你应该尽量减少对调用 API 的次数。

示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。 

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
'''

#-------例2--->   寻找峰值  <--------
'''
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。

示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5 
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

说明:你的解法应该是 O(logN) 时间复杂度的。

def findPeakElement(self,nums):
    """
    :type nums: List[int]
    :rtype: int
    """
'''

#-----例3---->  寻找旋转排序数组中的最小值 <----------
'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1

示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0

def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
'''

#--------模板3--------
'''
模板 #3 是二分查找的另一种独特形式。 它用于搜索需要访问当前索引及其在数组中的直接左右邻居索引的元素或条件。
'''
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: 
        return left
    if nums[right] == target: 
        return right
    return -1

#---关键属性----
'''
·  实现二分查找的另一种方法。
·  搜索条件需要访问元素的直接左右邻居。
·  使用元素的邻居来确定它是向右还是向左。
·  保证查找空间在每个步骤中至少有 3 个元素。
·  需要进行后处理。 当剩下 2 个元素时，循环 / 递归结束。 需要评估其余元素是否符合条件。
'''
# --- 区分语法-----
'''
·  初始条件：left = 0, right = length-1
·  终止：left + 1 == right
·  向左查找：right = mid
·  向右查找：left = mid
'''
#-------例1 ---->  在排序数组中查找元素的第一个和最后一个位置 <-----
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
'''
#-------例2 ---->  找到K个最接近的元素 <-----
'''
给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

示例 1:

输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]
 

示例 2:

输入: [1,2,3,4,5], k=4, x=-1
输出: [1,2,3,4]

def findClosestElements(self, arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
'''
# ------------小结-------------
'''
模板 #1 (left <= right)：

    · 二分查找的最基础和最基本的形式。
    · 查找条件可以在不与元素的两侧进行比较的情况下确定（或使用它周围的特定元素）。
    · 不需要后处理，因为每一步中，你都在检查是否找到了元素。如果到达末尾，则知道未找到该元素。
 

模板 #2 (left < right)：

    · 一种实现二分查找的高级方法。
    · 查找条件需要访问元素的直接右邻居。
    · 使用元素的右邻居来确定是否满足条件，并决定是向左还是向右。
    · 保证查找空间在每一步中至少有 2 个元素。
    · 需要进行后处理。 当你剩下 1 个元素时，循环 / 递归结束。 需要评估剩余元素是否符合条件。
 

模板 #3 (left + 1 < right)：

    · 实现二分查找的另一种方法。
    · 搜索条件需要访问元素的直接左右邻居。
    · 使用元素的邻居来确定它是向右还是向左。
    · 保证查找空间在每个步骤中至少有 3 个元素。
    · 需要进行后处理。 当剩下 2 个元素时，循环 / 递归结束。 需要评估其余元素是否符合条件。


时间：O(log n) —— 算法时间

因为二分查找是通过对查找空间中间的值应用一个条件来操作的，并因此将查找空间折半，在更糟糕的情况下，我们将不得不进行 O(log n) 次比较，其中 n 是集合中元素的数目。

空间：O(1) —— 常量空间

虽然二分查找确实需要跟踪 3 个指标，但迭代解决方案通常不需要任何其他额外空间，并且可以直接应用于集合本身，因此需要 O(1) 或常量空间。
'''
#-----例子---------
'''
1、 两个数组的交集_1

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]

示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]

说明:
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

2、两个数组的交集_2

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

3、两数之和--输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

4、寻找重复数
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2

示例 2:

输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n^2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
'''