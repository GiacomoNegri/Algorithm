inputs=[int(x) for x in input().split()]
modules=[int(x) for x in input().split()]

# Checking for capacity sufficiency
def is_cap_enough(c):
    curr_cap=0
    flights=1
    
    for i in range(inputs[0]):
        if modules[i]>c:
            return False
        elif curr_cap+modules[i]>c:
            flights+=1
            curr_cap=0
        
        curr_cap+=modules[i]
        
        if flights>inputs[1]:
            return False
    
    return True

# Binary search between capacities
right=sum(modules)
left=1
while left<right:
    mid=(right+left)//2
    if is_cap_enough(mid):
        right=mid
    else:
        left=mid+1
print(left)