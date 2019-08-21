'''
初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。
第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。

示例:

输入: 3
输出: 1 
解释: 
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 

你应该返回 1，因为只有一个灯泡还亮着。

'''
# ---------参考解-------------
'''
bulb代表第一轮结束后的所有灯亮灭的情况，从第二轮开始

    ·如果是最后一轮，则bulb的最后一个灯要switch
    ·对于其他轮，相应的第i-1+C(i)个灯要switch，且C为常数，i-1+C(i)必须<=n-1

'''
def bulbSwitch(self, n):
   
    bulb = [1] * n
    for i in range(2,n+1):
        for x in range(i-1, n, i):
            bulb[x] = 1 if bulb[x] == 0 else 0
    return bulb.count(1)

# ---------参考解2-------------
'''
A bulb ends up on iff it is switched an odd number of times.
Bulb i is switched in round d iff d divides i.
So bulb i ends up on iff it has an odd number of >divisors.
Divisors come in pairs, like i=12 has divisors 1 and 12, 2 and 6, and 3 and 4.
Except if i is a >square, like 36 has divisors 1 and 36, 2 and 18, 3 and 12, 4 and 9,
and double divisor 6. So bulb >i ends up on iff and only if i is a square. So just count the square numbers.

如果它被切换奇数次，则灯泡结束。
灯泡i在圆形d中切换如果d除以i。
因此，如果它有一个奇数个>除数，那么灯泡最终会结束。
除数成对出现，例如i = 12有除数1和12,2和6，以及3和4。
除非我是a> square，如36有除数1和36,2和18,3和12,4和9，
和双除数6.所以灯泡>我最终在iff上，只有我是一个正方形。 所以只计算平方数。
'''
'''
当一个灯泡被执行偶数次switch操作时它是灭着的，当被执行奇数次switch操作时它是亮着的，那么这题就是要找出哪些编号的灯泡会被执行奇数次操作。

现在假如我们执行第i次操作，即从编号i开始对编号每次+i进行switch操作，对于这些灯来说，
如果其编号j（j=1,2,3,⋯,n）能够整除i，则编号j的灯需要执行switch操作。

具备这样性质的i是成对出现的，比如：
    ·12 = 1 * 12，
    ·12 = 2 * 6
    ·12 = 3 * 4

所以编号为12的灯，在第1次，第12次；第2次，第6次；第3次，第4次一定会被执行Switch操作，这样的话，编号为12的灯执行偶数次switch，肯定为灭。
这样推出，完全平方数一定是亮着的，因为它有两个相同的因子，总因子数为奇数，如36 = 6 * 6，所以本题的关键在于找完全平方数的个数。

'''
def bulbSwitch(self, n):
    # The number of full/perfect squares.
    return int(math.sqrt(n))