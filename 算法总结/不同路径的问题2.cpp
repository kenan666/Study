/*
从起点 (x=0,y=0)(x=0,y=0) 出发，下一步只能向右或者向下到达第二点，向右则为 (x+1，y)(x+1，y) 向下则为 (x，y+1)(x，y+1)，
一直到 (x=m，y=n)(x=m，y=n) 这个点则为结束点视为一条路径。

因此从起点到终点的所有路径总数则为 22 个 以第二个点到终点的路径数的总和。

 */

// 递归求解
int uniquePaths(int m, int n)
{
    if(m <= 0 || n <= 0)
        return 0;
    else if(m == 1  || n == 1)//只能一直向右走或者一直向下走，所以路径数为 1
        return 1;
    else if(m == 2 && n == 2)
        return 2;
    else if((m == 3 && n == 2) || (m == 2 && n == 3))
        return 3;
    int paths = 0;
    paths += uniquePaths(m-1,n);
    paths += uniquePaths(m,n-1);
    return paths;
}

//简单优化  ******借鉴
int uniquePaths(int m, int n)
{
    if (m <= 0 || n <= 0)
        return 0;
    else if(m == 1  || n == 1)//只能一直向右走或者一直向下走，所以路径数为 1
        return 1;
    else if(m == 2 && n == 2)
        return 2;
    else if((m == 3 && n == 2) || (m == 2 && n == 3))
        return 3;
    if (a[m][n] > 0)
        return a[m][n]
    a[m-1][n] =  uniquePaths(m-1,n);
    a[m][n-1] =  uniquePaths(m,n-1);
    a[m][n] = a[m-1][n]+a[m][n-1];
    return a[m][n];

}