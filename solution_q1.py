import random
from collections import deque



def read(filepath):
    with open(filepath,'r') as file:
        for line in file:
            initial_str = line.strip().split(',')
    initial_lst = [0 if i=='_' else int(i) for i in initial_str]
    return initial_lst



# Function to print the current state of the puzzle as a string
def print_puzzle(state):
    state_str = ",".join(map(str, state)).replace("0", "_")
    print(state_str)



def find_possible_moves(state, empty_index):
    possible_moves = []

    # Define the possible moves (up, down, left, right)
    if empty_index >= 3:
        possible_moves.append(empty_index - 3)
    if empty_index < 6:
        possible_moves.append(empty_index + 3)
    if empty_index % 3 != 0:
        possible_moves.append(empty_index - 1)
    if empty_index % 3 != 2:
        possible_moves.append(empty_index + 1)
    
    return possible_moves



# Function to solve the 8-puzzle using random moves
def dfs(initial, goal):
    print("DFS path to solution:")

    state = initial
    moves = 0

    while state != goal:
        print_puzzle(state)

        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)
        move = random.choice(possible_moves)
        state[state.index(0)], state[move] = state[move], state[state.index(0)]
        moves += 1

    # Print goal state
    print_puzzle(state)



# Define the BFS function to solve the puzzle
def bfs(initial, goal):
    print("BFS path to solution:")

    queue = deque([initial])
    visited = set()

    while queue:
        state = queue.popleft()
        print_puzzle(state)
        
        if state == goal:
            break

        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)

        for move in possible_moves:
            new_state = state.copy()
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]

            if tuple(new_state) not in visited:
                visited.add(tuple(new_state))
                queue.append(new_state)



def ucs(initial, goal):
    pass



def a_star(initial, goal):
    pass



if __name__ == "__main__":
    # Input initial state as a list (e.g., [1, 2, 3, 4, 0, 5, 7, 8, 6])
    initial = read('input.txt')
    
    # Define the goal state
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # 0 represents the empty tile

    print("The solution of Q1.1 is:")
    print()
    
    #dfs(initial, goal)
    #print()
    
    bfs(initial, goal)
    print()

    ucs(initial, goal)
    print()

    a_star(initial, goal)
    print()



