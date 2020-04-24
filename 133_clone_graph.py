"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        pass

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors.append(n2)
print(n3.neighbors)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        og_node = node # has val 1
        og_q = [node]
        cloned_node = Node(1, []) # need to fill in all of its neighbors and its neighbors' neighbors, etc.
        cloned_q = [cloned_node]
        visited = set()
        while len(og_q):
            og = og_q.pop(0) # the og_node to visit
            cloned = cloned_q.pop(0) # the cloned_node to fill in its neighbor info
            visited.add(og.val)
            for og_neighbor in og.neighbors:
                if og_neighbor.val not in visited:
                    og_q.append(og_neighbor) # append to og_stack to keep BFSing
                    cloned_neighbor = Node(og_neighbor.val, [])
                    cloned.neighbors.append(cloned_neighbor)
                    cloned_neighbor.neighbors.append(cloned)
                    cloned_q.append(cloned_neighbor)
        print(cloned_node)
        return cloned_node