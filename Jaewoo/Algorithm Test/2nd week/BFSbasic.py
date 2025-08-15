map = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0] 
]

def mapFinding(x, y):
    stack = [(x,y)]
    wayStack = []
    while stack:
        a, b = stack.pop(0)
        if a not in range(5) or b not in range(6):
            continue
        if map[a][b] == 0: 
            map[a][b] = 1
            stack.append((a+1,b))
            stack.append((a-1,b))
            stack.append((a,b+1))
            stack.append((a,b-1))
            wayStack.append((a,b))
    return wayStack

print(mapFinding(0,0))