from collections import deque

def is_valid_state(missionaries, cannibals, boat):
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:
        return False
    if missionaries < 3 and (3 - missionaries) < (3 - cannibals):
        return False
    return True

def get_successors(state):
    successors = []
    m, c, b = state
    if b == 1:  # Boat on the original side
        new_states = [
            (m - 2, c, 0), (m - 1, c, 0), (m, c - 2, 0), (m, c - 1, 0), (m - 1, c - 1, 0)
        ]
    else:  # Boat on the opposite side
        new_states = [
            (m + 2, c, 1), (m + 1, c, 1), (m, c + 2, 1), (m, c + 1, 1), (m + 1, c + 1, 1)
        ]
    
    for state in new_states:
        if is_valid_state(*state):
            successors.append(state)
    
    return successors

def missionaries_and_cannibals():
    start_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    
    queue = deque([(start_state, [])])
    visited = set()
    visited.add(start_state)
    
    while queue:
        (current_state, path) = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]
        
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [current_state]))
    
    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Solution:")
        for state in solution:
            print(state)

if _name_ == "_main_":
    print("Missionaries and Cannibals Problem Solution")
    input("Press Enter to find the solution...")
    solution = missionaries_and_cannibals()
    print_solution(solution)
