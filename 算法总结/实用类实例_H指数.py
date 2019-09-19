#-----H 指数-----------
'''
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）
至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）”
 
示例:

输入: citations = [3,0,6,1,5]
输出: 3 
解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。

'''
#-------维基百科------
'''
H指数的计算基于其研究者的论文数量及其论文被引用的次数。赫希认为：一个人在其所有学术文章中有N篇论文分别被引用了至少N次，
他的H指数就是N。[1][2]如美国耶鲁大学免疫学家理查德·弗来沃发表的900篇文章中，有107篇被引用了107次以上，他的H指数是107。

可以按照如下方法确定某人的H指数：

1、将其发表的所有SCI论文按被引次数从高到低排序；
2、从前往后查找排序后的列表，直到某篇论文的序号大于该论文被引次数。所得序号减一即为H指数。
'''
def hIndex(citations):
    citations.sort(reverse = True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)

#---> 时间复杂度为O(logN)

#--------参考------桶排序

'''
因为『H指数』一定小于等于论文的数量n，所以我们把引用量大于论文数量的放在一起

我们准备 n + 1个桶，例题如下所示：

0    1         3        5、6
-    -    -    -    -    --
0    1    2    3    4    5  

'''
def hIndex(citations):
    n = len(citations)
    bucket = [0] * (n + 1)
    for citation in citations:
        if citation >= n:
            bucket[n] += 1
        else:
            bucket[citation] += 1
    #print(bucket)
    cur = 0
    for i in range(n, -1, -1):
        cur += bucket[i]
        if cur >= i:
            return i

#------H 指数 ||  ------------
'''
给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照升序排列。编写一个方法，计算出研究者的 h 指数。

h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）
至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"

示例:

输入: citations = [0,1,3,5,6]
输出: 3 
解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
     由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。

'''
#------参考 思路1  ----根据定义--------
def hIndex(citations):
    for idx, citation in enumerate(citations[::-1]):
        if idx >= citation:
            return idx
    return len(citations)

#-----------桶排序-------------
def hIndex( citations):
    n = len(citations)
    bucket = [0] * (n + 1)
    for citation in citations:
        if citation >= n:
            bucket[n] += 1
        else:
            bucket[citation] += 1
    #print(bucket)
    cur = 0
    for i in range(n, -1, -1):
        cur += bucket[i]
        if cur >= i:
            return i

# ------- 参考------思路3 -- 二分查找---------
'''
根据定义 citations 是递减的 ，我们找到从左边起，第一个索引号大于等于论文量的位置，所以 citations 是递增的，
然后再反过来。

'''
def hIndex(citations):
    n = len(citations)
    left = 0
    right = len(citations)
    while left < right:
        # print(left, right)
        mid = left + (right - left) // 2
        # n - mid 说明右边个数
        if citations[mid] < n - mid:
            left = mid + 1
        else:
            right = mid
    if left < n and citations[left] >= n - left: 
        return n - left
    return 0

#---------------------------------------------------------------------------
#---知识点补充---------
'''
桶排序（Bucket sort）或所谓的箱排序，是一个排序算法，工作的原理是将数组分到有限数量的桶里。
每个桶再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）。
桶排序是鸽巢排序的一种归纳结果。当要被排序的数组内的数值是均匀分配的时候，
桶排序使用线性时间O(n)（大O符号））。但桶排序并不是比较排序，他不受到 O(nlogn)下限的影响。

桶排序以下列程序进行：

1、设置一个定量的数组当作空桶子。
2、寻访序列，并且把项目一个一个放到对应的桶子去。
3、对每个不是空的桶子进行排序。
4、从不是空的桶子里把项目再放回原来的序列中。
'''
#----- python 实现------
def bucket_sort(array, n):
    # 1.创建n个空桶
    new_list = [[] for _ in range(n)]

    # 2.把arr[i] 插入到bucket[n*array[i]]
    for data in array:
        index = int(data * n)
        new_list[index].append(data)

    # 3.桶内排序
    for i in range(n):
        new_list[i].sort()

    # 4.产生新的排序后的列表
    index = 0
    for i in range(n):
        for j in range(len(new_list[i])):
            array[index] = new_list[i][j]
            index += 1
    return array
