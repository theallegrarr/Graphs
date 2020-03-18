from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node): 
  ancestor_tree = Graph()
  flattened = [item for sublist in ancestors for item in sublist]
  v = set(flattened)
  # add all unique vertices to graph
  for i in v:
    ancestor_tree.add_vertex(i)

  for rel in ancestors:
    # add edges backwards for a child => parent relationship
    ancestor_tree.add_edge(rel[1], rel[0])

  longest_path = 1
  earliest = -1
  # bfs/bft to find lontest path to topmost row of graph
  queue = Queue()
  queue.enqueue([starting_node])
  # visited = set()
  while queue.size() > 0:
    path = queue.dequeue()
    vertex = path[-1]
    # if vertex not in visited:
    #   visited.add(vertex)
    if len(path) == longest_path and vertex < earliest or len(path) > longest_path:
      earliest = vertex
      longest_path = len(path)
    for next_vert in ancestor_tree.get_neighbors(vertex):
      new_path = list(path)
      new_path.append(next_vert)
      queue.enqueue(new_path)
    print(f'path: {path}')
    print(f'vertex: {vertex}')
    # print(f"visited: {visited}")

  return earliest