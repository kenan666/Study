/*
假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m （1 ≤ m ≤ n） 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数。
如果不能使每台洗衣机中衣物的数量相等，则返回 -1。 

示例 1：
输入: [1,0,5]

输出: 3

解释: 
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2  

示例 2：
输入: [0,3,0]

输出: 2

解释: 
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1   
 
示例 3:
输入: [0,2,0]

输出: -1

解释: 
不可能让所有三个洗衣机同时剩下相同数量的衣物。

*/

/*
解题思路: 有四个洗衣机，装的衣服数为[0, 0, 11, 5]，最终的状态会变为[4, 4, 4, 4]，那么我们将二者做差，得到*[-4, -4, 7, 1]，
这里负数表示当前洗衣机还需要的衣服数，正数表示当前洗衣机多余的衣服数。我们要做的是*要将这个差值数组每一项都变为0，对于第一个洗衣机来说，
需要四件衣服可以从第二个洗衣机获得，那么就可以 把-4移给二号洗衣机，那么差值数组变为[0, -8, 7, 1]，此时二号洗衣机需要八件衣服，
那么至少需要移动8次。然后二号洗衣机把这八件衣服从三号洗衣机处获得，那么差值数组变为[0, 0, -1, 1]，此时三号洗衣机还缺1件，就从四号洗衣机处获得，
此时差值数组成功变为了[0, 0, 0, 0]，成功。那么移动的最大次数就是差值 数组中出现的绝对值最大的数字，8次

*/

//-------------参考2-------------------

/*
解题思路：
首先，先分析可以成立的情况，如果 衣服数量%机器总数 != 0，那么无法做到每一台机器都具有相同的衣服，
所以我们只需要分析能做到每台机器都具有平均数量衣服的情况。

接下来先求出这个平均值，设为k。
以机器中的某一个点i为例子进行分析，设i左边有a台机器，右边有b台机器，求出k * a - sum左和k * a - sum右，
如果小于0，说明这个区域多了衣服，若大于0，说明这个区域少了衣服。

         k 为平均每台机器应该有的衣服数
         a 机器      i      b机器
        k*a-sum左          k*a-sum右
      若>0，说明缺少衣服，若<0，说明多了衣服

*/
class Solution{
public:
    int findMinMoves(vector<int>& machines) 
    {
        if (machines.size() < 1) 
        {
            return -1;
        }
        int size = machines.size();
        int sum = 0;
        for (int i = 0; i < size; i++) 
        {
            sum += machines[i]; //生成预处理数组
        }
        if (sum % size != 0) 
        {
            return -1;
        }
        int avg = sum / size;
        int leftSum = 0;
        int res = 0;
        for (int i = 0; i < size; i++) 
        {
            int L = i * avg - leftSum;//i左边的需要的数目-累加和
            int R = (size - i - 1) * avg - (sum - leftSum - machines[i]);//i右边的需要数目-累加和

            if (L > 0 && R > 0) //如果L > 0，R > 0 ，则两边都少了衣服，瓶颈在于两者之和
            { 
                res = std::max(L + R, res);
            } 
            else //其它情况的瓶颈都在于两者的绝对值的最大值
            { 
                res = std::max(std::max(std::abs(L), std::abs(R)), res);
            }
            leftSum += machines[i];
        }
        return res;
    }
};
//-------------python --------
/*
def findMinMoves(machines):

    if len(machines) < 1:
        return -1

    size = len(machines)
    Sum = 0

    for i in range (size):
        Sum += machines[i] # 生成预处理数组
        #print(Sum)

    if Sum % size != 0:  # 判断 衣服数量 % 机器总数 ！= 0  是否等于0
        return -1

    avg = Sum / size  # 设置平均值 avg 
    leftsum,res= 0,0
    
    for i in range (size):
        L = i * avg -leftsum  # i左边的需要的数目-累加和
        R = (size - i - 1 ) * avg -(Sum - leftsum - machines[i]) # i右边的需要数目-累加和

        if L>0 and R>0 : # 如果L > 0，R > 0 ，则两边都少了衣服，瓶颈在于两者之和
            res = max(L+R,res)
        else:  #  其它情况的瓶颈都在于两者的绝对值的最大值
            res = max(max(abs(L),abs(R)),res)

        leftsum += machines[i]
    
    return res

*/