'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。 

示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

'''
# 暴力法
'''
直接的方法是遍历每个滑动窗口，找到每个窗口的最大值。一共有 N - k + 1 个滑动窗口，每个有 k 个元素，于是算法的时间复杂度为 O(Nk)

'''
def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
    n = len(nums)
    if n * k == 0:
        return []
    
    return [max(nums[i:i + k]) for i in range(n - k + 1)]

'''
时间复杂度：O(Nk)。其中 N 为数组中元素个数。

空间复杂度：O(N−k+1)，用于输出数组。
'''

# -------参考大佬---------------困难题********************
# 双向队列
'''
算法
    ·处理前 k 个元素，初始化双向队列。

    ·遍历整个数组。在每一步 :

    ·清理双向队列 :

        - 只保留当前滑动窗口中有的元素的索引。

        - 移除比当前元素小的所有元素，它们不可能是最大的。

    ·将当前元素添加到双向队列中。

    ·将 deque[0] 添加到输出中。

    ·返回输出数组。

'''
def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
    # base cases
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums
    
    def clean_deque(i):
        # remove indexes of elements not from sliding window
        if deq and deq[0] == i - k:
            deq.popleft()
            
        # remove from deq indexes of all elements 
        # which are smaller than current element nums[i]
        while deq and nums[i] > nums[deq[-1]]:
            deq.pop()
    
    # init deque and output
    deq = deque()
    max_idx = 0
    for i in range(k):
        clean_deque(i)
        deq.append(i)
        # compute max in nums[:k]
        if nums[i] > nums[max_idx]:
            max_idx = i
    output = [nums[max_idx]]
    
    # build output
    for i in range(k, n):
        clean_deque(i)          
        deq.append(i)
        output.append(nums[deq[0]])
    return output

#  时间复杂度 O(N) 每次元素被处理两次-其索引被添加到双向队列中和被双向队列删除
#  空间复杂度 O(N) 输出数组使用了O(N - k + 1)空间，双向队列使用了O(k)

# ------------另一种写法--------------
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    size = len(nums)

    # 特判
    if size == 0:
        return []
    # 结果集
    res = []
    # 滑动窗口，注意：保存的是索引值
    window = deque()

    for i in range(size):
        # 当元素从左边界滑出的时候，如果它恰恰好是滑动窗口的最大值
        # 那么将它弹出
        if i >= k and i - k == window[0]:
            window.popleft()

        # 如果滑动窗口非空，新进来的数比队列里已经存在的数还要大
        # 则说明已经存在数一定不会是滑动窗口的最大值（它们毫无出头之日）
        # 将它们弹出
        while window and nums[window[-1]] <= nums[i]:
            window.pop()
        window.append(i)

        # 队首一定是滑动窗口的最大值的索引
        if i >= k - 1:
            res.append(nums[window[0]])
    return res
