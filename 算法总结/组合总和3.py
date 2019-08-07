'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。
 
示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

'''

'''
1、回溯构造数套路基本是固定的。
2、回溯的题的精髓就是剪枝，去除那些不需要的递归情况能明显加速程序运行。
3、但是这道题的规模太小，回溯提升都不如官方服务器对结果的影响大。
4、可以设一个全局变量来观察程序递归了多少次，以此来看剪枝是否有效。

'''

'''
1、递归终止条件：数组中包含k个数，如果和为n则加入结果集，否则直接返回终止递归
2、递归过程：循环遍历1-9，将新数字加入临时数组中进入下一层递归，出来后再将其移除
'''
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    res = []
    path = []
    def helper(cur,path,cursum):
        if(len(path) == k and cursum == n):
            res.append(path[:])
        for i in range(cur,10):
            if(i+cursum > n): #剪枝的情况
                return
            path.append(i)
            helper(i+1,path,cursum+i)
            path.pop()
    helper(1,path,0)
    return res

#-----解2--------
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    def comb(k:int, n:int, start:int)->list:  # 从start考虑，可以避免重复
        if k == 1:    # 终止条件
            if n < 10:
                return [[n]]
            return []
        res = []
        for i in range(start+1, min((n+1)//2, 10)):  # 当前数最多取到n的一半，避免重复，且得满足i<10
            for j in comb(k-1, n-i, i):  # 回溯
                res.append([i]+j)
        return res
    return comb(k,n,0)
