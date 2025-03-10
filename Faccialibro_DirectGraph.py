from collections import deque

def bfs_distance(start,n,graph,visited):
    queue=deque()
    distance={start:0}

    visited[start-1]=True
    queue.append(start)
    
    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor-1]:
                visited[neighbor-1]=True
                queue.append(neighbor)
                distance[neighbor]=distance[node]+1
    return distance

def bfs(start,n,graph,visited):
    queue=deque()

    visited[start-1]=True
    queue.append(start)
    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor-1]:
                visited[neighbor-1]=True
                queue.append(neighbor)

def solver(lab,n,graph,vis_list):
    distance_dict=bfs_distance(lab,n,graph,vis_list)

    groups=1
    for i in range(n):
        if not vis_list[i]:
            bfs(i+1,n,graph,vis_list)
            groups+=1
    
    print(f'Acquaintances of {lab}:')

    lab_nodes=sorted(distance_dict.keys())
    for node in lab_nodes:
        if node!=lab:
            print(f'{node}: {distance_dict[node]}')
        
    print(f'There are {groups} groups.')

z = int(input())

for _ in range(z):
    n, m = [int(x) for x in input().split()]
    d = {}
    visited=[False]*n
    
    for _ in range(m):
        a, b = [int(x) for x in input().split()]
        
        if a not in d:
            d[a] = []
        if b not in d:
            d[b] = []
            
        d[a].append(b)
        d[b].append(a)
        
    label=int(input())
    solver(label, n, d, visited)