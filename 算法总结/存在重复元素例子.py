'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

'''
# --------- 集合法--------------
# 判断元数组和该数组的长度相不相等******************
def containsDuplicate(self, nums: List[int]) -> bool:
    return len((set(nums))) != len(nums)

# -----maphash ------------
'''

·使用set或HashMap解，原理相同，都是利用其查询某元素为O(1)时间复杂度；
    ·遍历nums，若set或HashMap中含有当前数字n，则直接返回true；
    ·直到遍历完毕，返回false。

'''
def containsDuplicate(self, nums: List[int]) -> bool:
    dic = {}
    for n in nums:
        if n in dic: 
            return True
        dic[n] = 1
    return False

# --------排序------------
# 排序之后，相等元素必相邻
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]:
            return True
    return False



# -----------存在重复元素2------------------
'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false

'''
#-------思路-------------
'''
1、判定重复元素，使用哈希表；

2、题目要求“ i 和 j 的差的绝对值最大为 k”，因此，哈希表的 key 为数组元素，value 为其对应的索引；

3、“是否存在问题”的做法是：在遍历的过程中找到就直接返回，如果找不到，才返回 false。因此找到（或者说存在）的充分必要条件是：

·找到重复元素的索引与之前出现过的这个元素的索引的差小于等于 k，后出现的数的索引一定比前出现的数的索引大，因此绝对值不用考虑。


'''
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # 判断存在重复元素的索引之差小于某个数
    # 先判断 nums [i] = nums [j]
    # 然后判断索引值是否相等，所以索引值可以用 map 存起来

    size = len(nums)
    if size == 0:
        return False

    map = dict()
    for i in range(size):
        if nums[i] in map and i - map[nums[i]] <= k:  # 只要找到 1 个符合题意的就返回
            return True        
        map[nums[i]] = i   # 更新为最新的索引，这里有贪心选择的思想，索引越靠后，符合题意的数据对的存在性就越大
    
    return False   # 遍历完成以后，都没有符合题意的时候，才返回 False

'''
·时间复杂度：O(N)，这里 NN 是数组的元素个数，算法遍历了一次数组。
·空间复杂度：O(N)，这里使用了哈希表存储已经出现的数，可以说是以空间换时间了。

'''

#---------存在重复元素3-------------------
'''
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

'''
# -----待定----