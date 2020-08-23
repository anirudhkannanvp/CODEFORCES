t = int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int,input().split()))
    mini=min(arr)
    arr2 = sorted(arr)
    st=0
    for i in range(n):
        if(arr[i]!=arr2[i] and arr[i]%mini!=0):
            st=1
            break
    if(st==1):
        print("NO")
    else:
        print("YES")
            