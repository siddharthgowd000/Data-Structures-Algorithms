def create_adjacency_list(n, m, edges):
    adj_list = {i: [] for i in range(n)}

    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)  # This line will be removed in case of a directed graph

    return adj_list

def print_adjacency_list(adj_list):
    for node, neighbors in adj_list.items():
        print("{} {}".format(node, ' '.join(map(str, neighbors))))

# Read input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Create adjacency list
adj_list = create_adjacency_list(n, m, edges)

# Print adjacency list
print_adjacency_list(adj_list)
