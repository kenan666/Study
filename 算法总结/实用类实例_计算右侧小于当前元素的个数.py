'''
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:
输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

'''
# -----------思路1 ---参考--------------
'''
思路:将给定数组从最后一个开始，用二分法插入到一个新的数组，这样新数组就是有序的，
那么此时该数字在新数组中的坐标就是原数组中其右边所有较小数字的个数，时间复杂度为O（nlogn）
'''
def countSmaller(self, nums: List[int]) -> List[int]:    
    ans = [0] * len(nums)
    helper = [] 
    for i in range(len(nums)-1, -1, -1):               
        idx = bisect.bisect_left(helper, nums[i])
        helper.insert(idx, nums[i])
        ans[i] = idx
    return ans

#----------参考-----------
def countSmaller(self, nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    ins = []                    #插排数组初始化
    t = 1
    for c in nums[:: -1]:       #逆序遍历
        k = bisect.bisect_left(ins, c)      #二分查找
        ins.insert(k, c)        #插入
        ans[-t] = k             #逆序输出答案
        t += 1
    return ans

# 优化
def countSmaller(self, nums: List[int]) -> List[int]:
    ans, ins = [], []           #插排数组初始化
    for c in nums[:: -1]:       #逆序遍历
        k = bisect.bisect_left(ins, c)
        ins.insert(k, c)
        ans.insert(0, k)
    return ans

