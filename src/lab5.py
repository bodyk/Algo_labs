from collections import defaultdict, deque

def topological_sort(dependencies, nodes):
    incoming_edges_degree = {node: 0 for node in nodes}
    for node, deps in dependencies.items():
        for dep in deps:
            incoming_edges_degree[dep] += 1
    
    # Queue for all nodes with no incoming edge
    queue = deque([node for node in nodes if incoming_edges_degree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        # Decrease the incoming_edges_degree of dependent nodes
        for dep in dependencies[node]:
            incoming_edges_degree[dep] -= 1
            if incoming_edges_degree[dep] == 0:
                queue.append(dep)

    if len(sorted_order) == len(nodes):
        return sorted_order
    else:
        return []  # There is a cycle

def process_documents(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    dependencies = defaultdict(list)
    nodes = set()

    for line in lines:
        a, b = line.strip().split()
        dependencies[b].append(a)
        nodes.update([a, b])

    sorted_docs = topological_sort(dependencies, nodes)

    with open(output_file, 'w') as file:
        for doc in sorted_docs:
            file.write(doc + '\n')

input_filename = 'src/govern.in'
output_filename = 'src/govern.out'
process_documents(input_filename, output_filename)