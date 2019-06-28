'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''
# 回溯法
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    visited = set()
    def backtrack(nums, tmp):
        if len(nums) == len(tmp):
            res.append(tmp)
            return
        for i in range(len(nums)):
            if i in visited or (i > 0 and i - 1 not in visited and nums[i-1] == nums[i]):
                continue
            visited.add(i)
            backtrack(nums, tmp + [nums[i]])
            visited.remove(i)
    backtrack(nums, [])
    return res

# 库函数法  itertools
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    return list({p for p in itertools.permutations(nums)})
