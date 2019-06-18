/*
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 */
/*
给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
 */

//  解 1
/*
使用两个指针，一个快指针 i 和一个慢指针 k 。i 每次移动一步，而 k 只在添加新的被需要的值时才移动一步。

因为新数组的长度会小于等于旧数组，调用者在调用函数时根据返回的长度，它会打印出数组中该长度范围（k）内的所有元素。因此，范围外的元素不会输出。

 */
int removeElement(vector<int>& nums, int val)
{
    int k = 0;
    for (int i=0; i < nums.size();i++)
    {
        if (nums[i] != nums[k])
        {
            nums[k] = nums[i];
            ++k;
        }
    }
    return k;
}

// 解2 覆盖法
//  python法
def removeElement(self, nums: List[int], val: int) -> int:
    idx = 0
    for i in range(len(nums)):
        if nums[i] != val:
            num[idx] = nums[i]
            idx += 1
    return idx 





/*
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。


示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2


示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

*/

//  解1 库函数方法  find（）函数
 int strStr(string haystack, string needle) 
 {
     if (neddle.empty())
        return 0;
    int pos = haystack.find(neddle):
    return pos;
 }


 //  解2 KMP算法求解
 def strStr(self, t, p):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not p : return 0
        _next = [0] * len(p)

        def getNext(p, _next):
            _next[0] = -1
            i = 0
            j = -1
            while i < len(p) - 1:
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]
        getNext(p, _next)
        i = 0
        j = 0
        while i < len(t) and j < len(p):
            if j == -1 or t[i] == p[j]:
                i += 1
                j += 1
            else:
                j = _next[j]
        if j == len(p):
            return i - j
        return -1

//  解 3  sunday  算法
//  来源于网络了解，了解不透彻
int strStr(string haystack, string needle) 
{
    if(needle.empty())
        return 0;
        
    int slen=haystack.size();
    int tlen=needle.size();
    int i=0,j=0;//i指向源串首位 j指向子串首位
    int k;
    int m=tlen;//第一次匹配时 源串中参与匹配的元素的下一位
    
    for(;i<slen;)
    {
        if(haystack[i]!=needle[j])
        {
            for(k=tlen-1;k>=0;k--)//遍历查找此时子串与源串[i+tlen+1]相等的最右位置
            {
                if(needle[k]==haystack[m])
                    break;
            }
            i=m-k;//i为下一次匹配源串开始首位 Sunday算法核心：最大限度跳过相同元素
            j=0;//j依然为子串首位
            m=i+tlen;//m为下一次参与匹配的源串最后一位元素的下一位
            if(m>slen)//当下一次参与匹配的源串字数的最后一位的下一位超过源串长度时
                return -1;
        }
        else
        {
            if(j==tlen-1)//若j为子串末位 匹配成功 返回源串此时匹配首位
                return i-j;
            i++;
            j++;
        }
    }
    return -1;//当超过源串长度时 
}
