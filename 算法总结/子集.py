'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
#思路一:库函数
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    for i in range(len(nums)+1):
        for tmp in itertools.combinations(nums, i):
            res.append(tmp)
    return res


#思路二:迭代
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res


#思路三:递归
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    
    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j + 1,tmp + [nums[j]] )
    helper(0, [])
    return res  


'''
其他情况:
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''
# 解1 递归
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    nums.sort()
    def helper(idx, tmp):
        res.append(tmp)
        for i in range(idx, n):
            if i > idx and nums[i] == nums[i-1]:
                continue
            helper(i+1, tmp + [nums[i]])
    helper(0, [])
    return res


# 迭代
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    if not nums: return []
    nums.sort()
    res = [[]]
    cur = []
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            cur = [tmp + [nums[i]] for tmp in cur]
        else:
            cur = [tmp + [nums[i]] for tmp in res]
        res += cur
    return res