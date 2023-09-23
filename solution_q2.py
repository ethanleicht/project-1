import random
import heapq
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

# Function to check if the current state satisfies the new goal test
def is_goal_state(state):
    top_row_sum = sum(state[:3])
    return top_row_sum == 11

# Function to solve the 8-puzzle using depth-first search
def dfs(initial):
    print("DFS path to solution:")

    state = initial[:]
    moves = 0

    while not is_goal_state(state):  # Check the new goal test
        print_puzzle(state)

        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)
        move = random.choice(possible_moves)
        state[state.index(0)], state[move] = state[move], state[state.index(0)]
        moves += 1

    # Print goal state
    print_puzzle(state)


def bfs(initial):
    print("BFS path to solution:")
    state = initial
    visited = set()
    queue = deque([(state, [])])

    while queue:
        state, path = queue.popleft()
        visited.add(tuple(state))

        print_puzzle(state)  # Print the current state

        if is_goal_state(state):
            print("Solution found!")
            print("Path to solution:")
            for step in path:
                print_puzzle(step)
            return

        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)

        for move in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            if tuple(new_state) not in visited:
                queue.append((new_state, path + [new_state]))

    print("No solution found!")


def ucs(initial):
    print("UCS path to solution:")
    state = initial
    visited = set()
    priority_queue = [(0, state, [])]

    while priority_queue:
        cost, state, path = heapq.heappop(priority_queue)
        if tuple(state) in visited:
            continue

        print_puzzle(state)  # Print the current state

        if is_goal_state(state):
            print("Solution found!")
            print("Path to solution:")
            for step in path:
                print_puzzle(step)
            return

        visited.add(tuple(state))

        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)

        for move in possible_moves:
            new_state = state[:]
            new_state[empty_index], new_state[move] = new_state[move], new_state[empty_index]
            heapq.heappush(priority_queue, (cost + 1, new_state, path + [new_state]))

    print("No solution found!")

if __name__ == "__main__":
    # Input initial state as a list (e.g., [1, 2, 3, 4, 0, 5, 7, 8, 6])
    #initial = read('input.txt')
    initial = [1, 3, 2, 4, 0, 5, 7, 8, 6]

    print("The solution of Q2.1 is:")
    print()
    
    dfs(initial)
    print()
    
    bfs(initial)
    print()

    ucs(initial)
    print()

    
