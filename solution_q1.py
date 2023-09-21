def read(filepath):
    with open(filepath,'r') as file:    
        for line in file:
            lst = line.strip().split(',')
    lst = [0 if i=='_' else int(i) for i in lst]
    return lst
    #return [lst[0:3],lst[3:6],lst[6:9]]



def main():
    init = read('input.txt')
    print(init)
    pos = init.index(0)
    goal=[0,1,2,3,4,5,6,7,8]
    #goal = [[None,1,2],[3,4,5],[6,7,8]]
    
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
    dfs(graph, pos)



def mydfs(init, goal):
    count = 0
    pos = init.index(0)
    state = init
    while state != goal and count < 100000:
        if pos not in [0,3,6]:
            state, pos = left(state, pos)
        elif pos not in [2,5,8]:
            state, pos = right(state, pos)
        count += 1



def dfs(graph, node, visited=set()):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)



def left(state, pos):
    state[pos]=state[pos-1]
    state[pos-1]=0
    return state, pos-1

def right(state, pos):
    state[pos]=state[pos+1]
    state[pos+1]=0
    return state, pos+1

def up(state, pos):
    state[pos]=state[pos-3]
    state[pos-3]=0
    return state, pos-3

def down(state, pos):
    state[pos]=state[pos+3]
    state[pos+3]=0
    return state, pos+3



if __name__ == "__main__":
    main()
