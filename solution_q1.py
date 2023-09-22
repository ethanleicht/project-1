def read(filepath):
    with open(filepath,'r') as file:    
        for line in file:
            lst = line.strip().split(',')
    lst = [0 if i=='_' else int(i) for i in lst]
    return lst



def main():
    init = read('input.txt')
    goal=[0,1,2,3,4,5,6,7,8]
    dfs(init, goal)

    
    # Using a Python dictionary to act as an adjacency list
    graph = {
        0 : [1,3],
        1 : [0,2,4],
        2 : [1,5],
        3 : [0,4,6],
        4 : [1,3,5,7],
        5 : [2,4,8],
        6 : [3,7],
        7 : [4,6,8],
        8 : [5,7]
    }
    #dfs(graph, pos)



def dfs(state, goal, prev=None):
    if state == goal:
        print('The solution of Q1.1 is:')    
    else:     
        print(state)
        pos = state.index(0)
        if pos not in [0,3,6] and prev != 'r':
            dfs(left(state.copy(), pos), goal, 'l')
        elif pos not in [2,5,8] and prev != 'l':
            dfs(right(state.copy(), pos), 'r')
        elif pos not in [0,1,2] and prev != 'd':
            dfs(up(state.copy(), pos), 'u')
        elif prev != 'u':
            dfs(down(state.copy(), pos), 'd')


def online_dfs(graph, node, visited=set()):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            online_dfs(graph, neighbour, visited)



def left(state, pos):
    state[pos]=state[pos-1]
    state[pos-1]=0
    return state

def right(state, pos):
    state[pos]=state[pos+1]
    state[pos+1]=0
    return state

def up(state, pos):
    state[pos]=state[pos-3]
    state[pos-3]=0
    return state

def down(state, pos):
    state[pos]=state[pos+3]
    state[pos+3]=0
    return state



if __name__ == "__main__":
    main()
