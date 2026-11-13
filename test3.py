"""
def solution(N, edges):
    # Your code here
    if not N:
        return 0
    merged_edges = [edges[0]]
    components = 1

    for i in range(0, len(edges) - 1):  
        current = merged_edges[-1]
        next = edges[i+1]

        if current[1] == next[0]:
            current[1] = next[1]
        else:
            merged_edges.append(next)
            components = components + 1

    return components





N = 5
edges = [[0, 1], [1, 2], [3, 4]]
comps = solution(N, edges)
print(comps)
"""
"""
def solution(N, edges):
    adj = [[] for _ in range(N)]
    visited = []

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    for i in range(N):
        visited.append(False)

    for i in adj:

"""

def solution(N, edges):
    #Initialization with empty lists
    adj_list = []
    components = 0

    for i in range(N):
        adj_list.append([])
    # adjacency list
    for u, v in edges:
        adj_list[u].append(v) 
        adj_list[v].append(u)
    # list that holds the visited nodes
    visited = []
    for i in range(N):
        visited.append(False)

    def dfs(node):
        visited[node] = True

        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)


    for node in range(N):
        if not visited[node]:
            components = components + 1
            dfs(node)

    return components






N = 5
edges = [[0, 1], [1, 2], [3, 4]]
res = solution(N, edges)
print(res)
