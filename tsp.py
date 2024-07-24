import itertools

def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities):
        total_distance += distance_matrix[route[i % num_cities]][route[(i + 1) % num_cities]]
    return total_distance

def travelling_salesman_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    all_cities = list(range(num_cities))
    shortest_route = None
    min_distance = float('inf')
    
    for route in itertools.permutations(all_cities):
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = route
    
    return shortest_route, min_distance

# Example usage:
if __name__ == "__main__":
    # Example distance matrix (replace with your actual distance matrix)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    shortest_route, min_distance = travelling_salesman_brute_force(distance_matrix)
    
    print("Shortest Route:", shortest_route)
    print("Minimum Distance:", min_distance)
