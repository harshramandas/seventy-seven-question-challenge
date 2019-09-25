#     0   1   2   3
# 0   0   1   1   0
# 1   0   0   1   0
# 2   1   0   0   1
# 3   0   0   0   1
def DFS(matrix):
    n = len(matrix[0])
    visited = [0]*n
    stack = [0] #Node 0 as source
    visited[0] = 1 #Node  as visited
    node = stack.pop() #dequeue for queue pop(0); pop for stack pop()
    print(node)

    while True:
        for x in range(0, n):
            #Check if route exists and node not visited
            if matrix[node][x] == 1 and visited[x] == 0:
                visited[x] = 1 # Visit node
                stack.append(x)
        if len(stack) == 0:
            break
        else:
            node = stack.pop() #Pop element from stack
            print(node)
matrix =  [[0,1,1,0],[0,0,1,0],[1,0,0,1],[0,0,0,1]]
DFS(matrix)