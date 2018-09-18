def dfs(G, current_vert, visited):
    visited[current_vert] = True
    print('Traversal: ' + current_vert.get_vertex_id())
    for nbr in current_vert.get_connections():
        if nbr not on visited:
            dfs(G, nbr, visited)

def dfs_traversal(G):
    visited = {}
    for current_vert in G:
        if current_vert not in visited:
            dfs(G, current_vert, visited)
