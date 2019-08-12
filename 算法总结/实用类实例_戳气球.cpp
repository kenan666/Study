/* ----------困难----------------------

有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

示例:
输入: [3,1,5,8]
输出: 167 
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

*/
// ----------参考-------------
//  思路

/*
记忆化搜索（递归 + 动态规划）。
nums数组首和尾各扩增一个数值1，以便于计算。

设二维数组dp[start][end],表示扩增后nums数组下标start到end的dp值（即[start,end]区间里能获得硬币的最大数量）。假设下标middle指示的位置为
这个区间里最后一个戳破气球的位置，则dp[start][middle-1]表示该位置左半部分已经戳破气球得到的奖赏，dp[middle+1][end]表示该位置右半部分已经
戳破气球得到的奖赏。此时middle位置上的气球与(start-1)，(end+1)位置上的气球相邻,最后戳破middle位置上的气球，因而得到的总奖赏为:
nums[start-1]*nums[middle]*nums[end+1] + dp[start][middle-1] + dp[middle+1][end];

对于[start,end]区间每一个位置都尝试作为最后一个戳破的气球位置,寻找总奖赏最大的作为该区间的dp值，并记录，以便下次用到该区间时，dp值不需重新计算。
特殊情况:当middle指向start或end位置时，继续递归会出现start > end 的情况，此时只需返回0。

*/

class Solution {
private:
    vector<vector<int>> dp;
    vector<int> mnums;
public:
    int maxCoins(vector<int>& nums) {
        if(nums.empty())
            return 0;
        int n;
        nums.insert(nums.begin(), 1);
        nums.insert(nums.end(), 1);
        n = nums.size();
        dp = vector<vector<int>>(n, vector<int>(n, 0));   //初始化所有区间dp值为0
        mnums = nums;                                     //复制nums数组为类成员变量
        return dfs(1, n-2);
    }
    int dfs(int start, int end){
        int middle, left, right;
        if(start > end)                                   //特殊情况
            return 0;
        if(dp[start][end] != 0)                           //备忘录中记录有该数据，返回该数据，不必从新计算
            return dp[start][end];
        for(middle = start; middle <= end; ++middle){     //对区间的每一个位置尝试性作为最后一个戳破的位置，找到最优的位置
            left = dfs(start, middle-1);                  //区间[start，middle-1]的dp值
            right = dfs(middle+1, end);                   //区间[middle+1，end]的dp值
            dp[start][end] = max(dp[start][end], left + right + mnums[start-1] * mnums[middle] * mnums[end+1]);   //加入备忘录
        }
        return dp[start][end];
    }
};


// --------参考学习---------------
/*
回溯法
           3  1  5
         /    |   \
        1 5  3 5  3 1      3(n)
        / \  /  \ /  \ 
        5  1 5  3 1   3    2(n-1)

        方案总数 ： n * (n-1) * (n-2) *·····*1 = n!
        函数调用次数 ：1+ n + n*(n-1) + n*(n-1)(n-2) + ···· + n!
超时

*/
class Solution {
private:
void helper(vector<int> & nums ,int coins,int & ans){
    //  boundary
    if (nums.size() == 0){
        ans = max(ans,coins);
        return ;
    }
    //search
    for (int i = 0;i<nums.size();++i){
        int tmp = nums[i];
        int delta = nums[i] * (i-1<0 ? 1 : nums[i-1]) * (i + 1>nums.size() - 1 ? : nums[i+1]);
        nums.erase(nums.begin() + i);
        helper(nums,coins + delta,ans);
        nums.insert(nums.begin() + i,tmp);
    }
}

public:
    int maxCoins(vector<int>& nums) {
        int ans = 0;
        helper(nums,0,ans);
        return ans;
    }
};

//-----动态规划求解---------- 
/*
动态规划---记忆化递归（备忘录法）

分析最优子结构

正向思考

以[3,1,5] 为例，对于第一次选择，我们有三种选择
·选择3，将问题分为左边的子问题，[] 和右边子问题：[1,5]
    其解等于 [] + [1,5] +1 *3 * 1
·选择1，将问题分为左边的子问题，[3] 和右边子问题：[5]
    其解等于 [3] + [5] +3 * 1 * 5
·选择3，将问题分为左边的子问题，[3,1] 和右边子问题：[]
    其解等于 [3,1] + [] +1 *5 * 1

在其解题过程中，发现此解错误， 在正向思考的情况下，以选择1为例，在点爆1气球后，两个左右子问题并不独立，此时给子问题的求解带来了问题？？？

***---逆向思考----***
以[3,1,5]为例，首先拿一个气球，把这个气球当做最后一个气球，然后点爆它。这样就能够将这个气球的左右两个子问题独立开。。

换言之，我们选 1 气球的时候，然后优先点爆左边和右边的气球之后，再最后点爆这个气球，这是可以看出左右两个子问题是独立的，他们只和 1 这个气球有关联、

得到状态转移方程：
dp[i][j] 从i到j个气球（闭区间）能够获取的最大的硬币数量
dp[i][j] = dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1] (i<=k<=j)

方案总数仍然是O(n!),但是由于利用了“记忆化”的特征，将重复的子问题写在了内存中，保证了每一个种子问题只计算一遍。
*/
class Solution {
private:
    vector<vector<int>> dp;
    int helper(vector<int>&nums,int i,int j){
        //boundary
        if (i>j) return 0;
        if(dp[i][j] > 0) return dp[i][j];

        //search
        for (int k = i;k<=j;++k){
            int left = helper(nums,i,k-1);
            int right = helper(nums,k+1,j);
            int delta = nums[k] * nums[i-1] * nums[j+1];
            dp[i][j] = max(dp[i][j] , left + right + delta)
        }
        return dp[i][j];
    }
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        nums.insert(nums.begin(),1);
        nums.push_back(1);
        dp = vector<vector<int>>(n+2,vector<int>(n+2,0));
        int ans = helper(nums,1,n);
        return ans;
    }
};

//-----解3 自底向上----------参考---------
/*

自底向上，所有明确计算粒度： 从i到j，第一个长度是1，第二个长度2 ，直到长度为n

第一层 循环定义长度 len from 1 to n
第二层 循环定义遍历范围 1 to n-len+1 此时定义j的位置 j=i+len-1
第三层 在当前情况下，选取k个气球，当做是最后一个点爆，一共有k中选择 (i <= k <= j),选取最大值

返回dp[1][n]

*/
class Solution {

public:
    int maxCoins(vector<int>& nums) {
        vector<vector<int>> dp = vector<vector<int>>(n+2, vector<int>(n+2,0));

        int n = nums.size();
        nums.insert(nums.begin(),1);
        nums.push_back(1);

        for (int len = 1;len <= n; ++len){
            // i < n-len(n-1)+1
            for (int i = 1; i<= n-len+1 ; ++i){
                int j = i+len-1;
                for (int k =i; k <= j; ++k){
                    dp[i][j] = max(dp[i][j] ,dp[i][k-1] + dp[k+1][j] + nums[k] * nums[i-1] * nums[j+1]);
                }
            }
        }
        return dp[1][n];
    }
};