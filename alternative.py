import heapq
from collections import deque

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __str__(self):
        return "\n".join([" ".join(map(lambda x: str(x) if x is not None else '_', self.state[i:i+3])) for i in range(0, 9, 3)])

    def manhattan_distance(self):
        distance = 0
        for i in range(8):
            if self.state[i] is not None:
                current_row, current_col = i // 3, i % 3
                target_index = self.state.index(i + 1)
                target_row, target_col = target_index // 3, target_index % 3
                distance += abs(current_row - target_row) + abs(current_col - target_col)
        return distance

    def straight_line_distance(self):
        distance = 0
        for i in range(8):
            if self.state[i] is not None:
                current_row, current_col = i // 3, i % 3
                target_index = self.state.index(i + 1)
                target_row, target_col = target_index // 3, target_index % 3
                distance += ((current_row - target_row) ** 2 + (current_col - target_col) ** 2) ** 0.5
        return distance

    def heuristic(self):
        # Use Manhattan distance heuristic by default
        return self.manhattan_distance()

def is_goal(state):
    return state == [None, 1, 2, 3, 4, 5, 6, 7, 8]

def find_blank(state):
    return state.index(None)

def actions(state):
    blank_index = find_blank(state)
    possible_actions = []
    if blank_index % 3 > 0:
        possible_actions.append('left')
    if blank_index % 3 < 2:
        possible_actions.append('right')
    if blank_index >= 3:
        possible_actions.append('up')
    if blank_index < 6:
        possible_actions.append('down')
    return possible_actions

def apply_action(state, action):
    new_state = state[:]
    blank_index = find_blank(new_state)
    if action == 'left':
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
    elif action == 'right':
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
    elif action == 'up':
        new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
    elif action == 'down':
        new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
    return new_state

def dfs(initial_state):
    explored = set()
    stack = [PuzzleNode(initial_state)]
    while stack:
        current_node = stack.pop()
        explored.add(tuple(current_node.state))
        if is_goal(current_node.state):
            return build_path(current_node)
        for action in actions(current_node.state):
            child_state = apply_action(current_node.state, action)
            if tuple(child_state) not in explored:
                child_node = PuzzleNode(child_state, current_node, action, current_node.cost + 1)
                stack.append(child_node)
    return None

def bfs(initial_state):
    explored = set()
    queue = deque([PuzzleNode(initial_state)])
    while queue:
        current_node = queue.popleft()
        explored.add(tuple(current_node.state))
        if is_goal(current_node.state):
            return build_path(current_node)
        for action in actions(current_node.state):
            child_state = apply_action(current_node.state, action)
            if tuple(child_state) not in explored:
                child_node = PuzzleNode(child_state, current_node, action, current_node.cost + 1)
                queue.append(child_node)
    return None


def ucs(initial_state):
    explored = set()
    priority_queue = [PuzzleNode(initial_state, None, None, 0)]
    heapq.heapify(priority_queue)
    
    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        explored.add(tuple(current_node.state))
        
        if is_goal(current_node.state):
            return build_path(current_node)
        
        for action in actions(current_node.state):
            child_state = apply_action(current_node.state, action)
            if tuple(child_state) not in explored:
                child_node = PuzzleNode(child_state, current_node, action, current_node.cost + 1)
                heapq.heappush(priority_queue, child_node)



def astar_manhattan(initial_state):
    explored = set()
    priority_queue = [PuzzleNode(initial_state, None, None, 0)]
    heapq.heapify(priority_queue)
    
    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        explored.add(tuple(current_node.state))
        
        if is_goal(current_node.state):
            return build_path(current_node)
        
        for action in actions(current_node.state):
            child_state = apply_action(current_node.state, action)
            if tuple(child_state) not in explored:
                child_node = PuzzleNode(child_state, current_node, action, current_node.cost + 1)
                heapq.heappush(priority_queue, child_node)
    
    return None

def astar_straight_line(initial_state):
    explored = set()
    priority_queue = [PuzzleNode(initial_state, None, None, 0)]
    heapq.heapify(priority_queue)
    
    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        explored.add(tuple(current_node.state))
        
        if is_goal(current_node.state):
            return build_path(current_node)
        
        for action in actions(current_node.state):
            child_state = apply_action(current_node.state, action)
            if tuple(child_state) not in explored:
                child_node = PuzzleNode(child_state, current_node, action, current_node.cost + 1)
                heapq.heappush(priority_queue, child_node)
    
    return None

def build_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    return list(reversed(path))

if __name__ == "__main__":
    # Initial state with '_'
    initial_state = [1, 4, 2, 3, None, 5, 6, 7, 8]

    # Solve the puzzle using DFS
    dfs_solution_path = dfs(initial_state)
    if dfs_solution_path:
        print("DFS Solution found:")
        dfs_actions_taken = [node.action for node in dfs_solution_path[1:]]  # Exclude the initial state
        print("Actions taken for the empty tile (DFS):", ", ".join(dfs_actions_taken))
        for step, node in enumerate(dfs_solution_path):
            print(f"Step {step}:")
            print(node.state)
            print()
    else:
        print("DFS: No solution found.")

    # Solve the puzzle using BFS
    bfs_solution_path = bfs(initial_state)
    if bfs_solution_path:
        print("\nBFS Solution found:")
        bfs_actions_taken = [node.action for node in bfs_solution_path[1:]]  # Exclude the initial state
        print("Actions taken for the empty tile (BFS):", ", ".join(bfs_actions_taken))
        for step, node in enumerate(bfs_solution_path):
            print(f"Step {step}:")
            print(node.state)
            print()
    else:
        print("BFS: No solution found.")

    ucs_solution_path = ucs(initial_state)
    if ucs_solution_path:
        print("UCS Solution found:")
        ucs_actions_taken = [node.action for node in ucs_solution_path[1:]]  # Exclude the initial state
        print("Actions taken for the empty tile (UCS):", ", ".join(ucs_actions_taken))
        for step, node in enumerate(ucs_solution_path):
            print(f"Step {step}:")
            print(node.state)
            print()
    else:
        print("UCS: No solution found.")
    
    # Solve the puzzle using A* with Manhattan distance heuristic
    astar_manhattan_solution_path = astar_manhattan(initial_state)
    if astar_manhattan_solution_path:
        print("\nA* Solution found (Manhattan Heuristic):")
        astar_manhattan_actions_taken = [node.action for node in astar_manhattan_solution_path[1:]]  # Exclude the initial state
        print("Actions taken for the empty tile (A* - Manhattan):", ", ".join(astar_manhattan_actions_taken))
        for step, node in enumerate(astar_manhattan_solution_path):
            print(f"Step {step}:")
            print(node.state)
            print("Manhattan Distance:", node.manhattan_distance())
            print()
    else:
        print("A* - Manhattan: No solution found.")
    
    # Solve the puzzle using A* with Straight Line Distance heuristic
    astar_straight_line_solution_path = astar_straight_line(initial_state)
    if astar_straight_line_solution_path:
        print("\nA* Solution found (Straight Line Heuristic):")
        astar_straight_line_actions_taken = [node.action for node in astar_straight_line_solution_path[1:]]  # Exclude the initial state
        print("Actions taken for the empty tile (A* - Straight Line):", ", ".join(astar_straight_line_actions_taken))
        for step, node in enumerate(astar_straight_line_solution_path):
            print(f"Step {step}:")
            print(node.state)
            print("Straight Line Distance:", node.straight_line_distance())
            print()
    else:
        print("A* - Straight Line: No solution found.")
