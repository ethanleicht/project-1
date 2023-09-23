import random


# Function to check if the current state satisfies the new goal test
def is_goal_state(state):
    top_row_sum = sum(state[:3])
    return top_row_sum == 11

# Function to solve the 8-puzzle using depth-first search
def dfs(initial, goal):
    print("DFS path to solution:")

    state = initial
    moves = 0

    while not is_goal_state(state):
        print_puzzle(state)

        empty_index = state.index(0)
        possible_moves = find_possible_moves(state, empty_index)
        move = random.choice(possible_moves)
        state[state.index(0)], state[move] = state[move], state[state.index(0)]
        moves += 1

    # Print goal state
    print_puzzle(state)

# ... (rest of the code)
