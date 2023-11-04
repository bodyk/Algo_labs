def read_adjacency_list(file_path):
    with open(file_path, 'r') as file:
        graph = {}
        for line in file:
            vertex, edges = line.strip().split(':')
            graph[vertex.strip()] = [e.strip() for e in edges.split()]
    return graph

def find_roots(graph):
    # Всі вершини у графі є потенційними коренями спочатку
    potential_roots = set(graph.keys())
    # Перебираємо всі ребра і видаляємо цільові вершини з потенційних коренів
    for edges in graph.values():
        for edge in edges:
            potential_roots.discard(edge)
    return list(potential_roots)

file_path = 'src/input.txt'
graph = read_adjacency_list(file_path)

root_vertices = find_roots(graph)

with open('src/output.txt', 'w') as f:
    if root_vertices:
        for root in root_vertices:
            f.write(f'{root}\n')
    else:
        f.write('-1\n')

if root_vertices:
    print(f'Root vertices: {root_vertices}')
else:
    print('No root vertices found. Written -1 to output.txt')
