'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

'''
# 思路1  自底向上
def climbStairs(self, n: int) -> int:
    if n <= 0 :
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    one_step_before = 2
    two_step_before = 1
    all_ways = 0
    for i in range (2,n):
        all_ways = one_step_before + two_step_before
        two_step_before = one_step_before
        one_step_before = all_ways
    return all_ways


# 自顶向下
def climbStairs(self, n: int) -> int:
    if n== 0 : return 1
    if n== 1 : return 1
    return self.climbStairs(n-1) + self.climbStairs(n-2)