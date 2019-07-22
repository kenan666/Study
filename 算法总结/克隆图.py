'''
给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。图中的每个节点都包含它的值 val（Int） 和其邻居的列表（list[Node]）。

示例：

1---2
|   |
4---3

输入：
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},
{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

解释：
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。

'''
# 深度优先遍历
def cloneGraph(self, node: 'Node') -> 'Node':
    lookup = {}

    def dfs(node):
        #print(node.val)
        if not node: return
        if node in lookup:
            return lookup[node]
        clone = Node(node.val, [])
        lookup[node] = clone
        for n in node.neighbors:
            clone.neighbors.append(dfs(n))        
        return clone

    return dfs(node)


#----------------------深度优先  参考大佬----------------------------
def cloneGraph(self, node: 'Node') -> 'Node':
    from collections import deque
    lookup = {}

    def bfs(node):
        if not node: return
        clone = Node(node.val, [])
        lookup[node] = clone
        queue = deque()
        queue.appendleft(node)
        while queue:
            tmp = queue.pop()
            for n in tmp.neighbors:
                if n not in lookup:
                    lookup[n] = Node(n.val, [])
                    queue.appendleft(n)
                lookup[tmp].neighbors.append(lookup[n])
        return clone

    return bfs(node)

