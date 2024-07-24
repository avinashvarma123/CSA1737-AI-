import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node in the path
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic estimate from current node to goal node
    
    def f(self):
        return self.g + self.h

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def astar_search(start_state, goal_state, neighbors_fn, heuristic_fn):
    start_node = Node(state=start_state, g=0, h=heuristic_fn(start_state, goal_state))
    frontier = PriorityQueue()
    frontier.put(start_node, start_node.f())
    came_from = {}
    cost_so_far = {start_state: 0}
    
    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state
        
        if current_state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = came_from.get(current_node.state)
            path.reverse()
            return path
        
        for next_state in neighbors_fn(current_state):
            new_cost = cost_so_far[current_state] + 1  # Assuming uniform cost
            
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + heuristic_fn(next_state, goal_state)
                next_node = Node(state=next_state, parent=current_node, g=new_cost, h=heuristic_fn(next_state, goal_state))
                frontier.put(next_node, priority)
                came_from[next_state] = current_node
    
    return None  # No path found

# Example usage:
def example_neighbors(state):
    # Define neighbors function, e.g., for a grid
    x, y = state
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    # Filter valid neighbors (e.g., within grid bounds)
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < 5 and 0 <= ny < 5]

def example_heuristic(state, goal_state):
    # Define heuristic function, e.g., Euclidean distance for a grid
    x1, y1 = state
    x2, y2 = goal_state
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

start = (0, 0)
goal = (4, 4)
path = astar_search(start, goal, example_neighbors, example_heuristic)
print("Path found:", path)
