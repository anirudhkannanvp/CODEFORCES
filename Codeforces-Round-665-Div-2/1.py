t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    if(n==k):
        print(0)
    elif(k==0):
        print(int(n%2))
    elif(k<n):
        print(int((a+k)//2))
    else:
        print(abs(k-n))
