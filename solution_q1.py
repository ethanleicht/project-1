def read(filepath):
    with open(filepath,'r') as file:
        for line in file:
            return line.strip()

def main():
    init = read('input.txt')
    goal = '_,1,2,3,4,5,6,7,8'

def dfs(init, goal):
    pass

if __name__ == "__main__":
    main()
