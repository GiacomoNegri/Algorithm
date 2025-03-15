from collections import deque

def find_best(n,k, existing_pers):
    visited=set(existing_pers)

    queue=deque(visited)
    dist={x:0 for x in visited}

    best_pers=None
    max_distance=-1

    while queue:
        curr=queue.popleft()
        curr_dist=dist[curr]
        
        for i in range(k):
            neigh=curr^(1<<i)
            if neigh not in visited:
                visited.add(neigh)
                dist[neigh]=curr_dist+1
                queue.append(neigh)

            if dist[neigh]>max_distance:
                max_distance=dist[neigh]
                best_pers=neigh
    
    return format(best_pers, f'0{k}b')
        

n, k = [int(x) for x in input().split()]
players=[0]*n
for i in range(n):
    players[i]=int(input().strip(), 2)

print(find_best(n,k,players))