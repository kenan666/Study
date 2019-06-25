'''
回溯法（英语：backtracking）是暴力搜索法中的一种。

对于某些计算问题而言，回溯法是一种可以找出所有（或一部分）解的一般性算法，尤其适用于约束满足问题（在解决约束满足问题时，我们逐步构造更多的候选解，
并且在确定某一部分候选解不可能补全成正确解之后放弃继续搜索这个部分候选解本身及其可以拓展出的子候选解，转而测试其他的部分候选解）。

在经典的教科书中，八皇后问题展示了回溯法的用例。（八皇后问题是在标准国际象棋棋盘中寻找八个皇后的所有分布，使得没有一个皇后能攻击到另外一个。）

回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，
再通过其它的可能的分步解答再次尝试寻找问题的答案。回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：

找到一个可能存在的正确的答案
在尝试了所有可能的分步方法后宣告该问题没有答案
在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

'''
'''
回溯方法试图通过尝试几种选择之一来找到解决方案。如果选择证明不正确，则计算在选择点回溯或重新启动，并尝试另一种选择。

回溯最广泛的用途是执行正则表达式。例如，简单模式“a * a”将无法与没有回溯的序列“a”匹配（因为，在第一次传递中，“a”被“a *”吃掉，留下任何后面的剩余“a”匹配。）
回溯的另一种用法是文本解析应用程序，解决迷宫，机器人等。
'''

'''
1、基本思想
   在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根结点出发深度探索解空间树。当探索到某一结点时，要先判断该结点是否包含问题的解，
   如果包含，就从该结点出发继续探索下去，如果该结点不包含问题的解，则逐层向其祖先结点回溯。（其实回溯法就是对隐式图的深度优先搜索算法）。

       若用回溯法求问题的所有解时，要回溯到根，且根结点的所有可行的子树都要已被搜索遍才结束。

       而若使用回溯法求任一个解时，只要搜索到问题的一个解就可以结束。

2、用回溯法解题的一般步骤：
    （1）针对所给问题，确定问题的解空间：

            首先应明确定义问题的解空间，问题的解空间应至少包含问题的一个（最优）解。

    （2）确定结点的扩展搜索规则

    （3）以深度优先方式搜索解空间，并在搜索过程中用剪枝函数避免无效搜索。
'''

'''
其实回溯算法关键在于:不合适就退回上一步

然后通过约束条件, 减少时间复杂度.

'''

# 例子1
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''
# 思路1
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    n = len(candidates)
    res = []
    def helper(i, tmp_sum, tmp):
        if tmp_sum > target or i == n:
            return 
        if tmp_sum == target:
            res.append(tmp)
            return 
        helper(i,  tmp_sum + candidates[i],tmp + [candidates[i]])
        helper(i+1, tmp_sum ,tmp)
    helper(0, 0, [])
    return res
#  思路2
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    n = len(candidates)
    res = []
    def backtrack(i, tmp_sum, tmp):
        if  tmp_sum > target or i == n:
            return 
        if tmp_sum == target:
            res.append(tmp)
            return 
        for j in range(i, n):
            if tmp_sum + candidates[j] > target:
                break
            backtrack(j,tmp_sum + candidates[j],tmp+[candidates[j]])
    backtrack(0, 0, [])
    return res

#  exam 2
'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

'''
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    if not candidates:
        return []
    candidates.sort()
    n = len(candidates)
    res = []
    
    def backtrack(i, tmp_sum, tmp_list):
        if tmp_sum == target:
            res.append(tmp_list)
            return 
        for j in range(i, n):
            if tmp_sum + candidates[j]  > target : break
            if j > i and candidates[j] == candidates[j-1]:continue
            backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])
    backtrack(0, 0, [])    
    return res

# exam 3
'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''
#  思路1
# 库函数  Python3 itertools 文档
def permute(self, nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))

#思路2 回溯

def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return 
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
    backtrack(nums, [])
    return res

# exam 4
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
# 思路1 库函数
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    return list({p for p in itertools.permutations(nums)})

# 思路2 回溯
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

# exam 5
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
#  思路1  库函数
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    for i in range(len(nums)+1):
        for tmp in itertools.combinations(nums, i):
            res.append(tmp)
    return res

# 思路2  迭代

def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    for i in nums:
        res = res + [[i] + num for num in res]
    return res

# 思路3 回溯
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    
    def helper(i, tmp):
        res.append(tmp)
        for j in range(i, n):
            helper(j + 1,tmp + [nums[j]] )
    helper(0, [])
    return res  

# exam 6
'''
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
# 思路1  迭代

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

# 思路2  递归
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
