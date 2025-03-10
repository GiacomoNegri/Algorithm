def closest_day(arr, target):
    left,right=0,len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    
    if right<0:
        return arr[left]
    elif left>=len(arr):
        return arr[right]
    else:
        return arr[left] if abs(target-arr[left])<abs(arr[right]-target) else arr[right]

# Execution
z=int(input())
for _ in range(z):
    n=int(input())
    d=[int(x) for x in input().split()]
    # =list(map(int, input.spli()))
    k=int(input())
    q=[int(x) for x in input().split()]
    
    # Sorting the lists
    answers=q[:]
    d.sort()
    q=list(set(q))
    
    # Computing the closest date
    matches={}
    for query in q:
        if query not in matches:
            matches[query]=closest_day(d,query)
        # print(matches)
    answers=[matches[query] for query in answers]
    print(' '.join(map(str, answers)))