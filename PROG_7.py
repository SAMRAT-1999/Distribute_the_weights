'''
Distribute the weights:
1                 #test case
5 3               #values in array          groups
1 2 3 4 5

Logic: minimum of maximum number in group
1  2   3 4 5            1 2   3 4   5            1 2 3    4    5
1  2     12               3     7   5              6      4    5
     12                        7                        6
                              6

Output:6
'''
def possible(arr,m,k):
     curr_sub= arr[0]
     subs=1
     flag=True
     for i in range(1,len(arr)):
          if arr[i]+curr_sub>k:
               curr_sub=arr[i]
               subs=subs+1
          else:
               curr_sub= arr[i] + curr_sub
          if(subs>m):
               flag= False
               break
     return(flag)

t=int(input())
for i in range(t):
    imp=list(map(int,input().split()))
    m=imp[1]
    arr=list(map(int,input().split()))
    left=max(arr)
    right=sum(arr)
    mid=(left+right)//2
    ans=[]
    while(left<=right):
        if(possible(arr,m,mid)):
            ans.append(mid)
            right=mid-1
        else: 
            left=left+1
        mid=(left+right)//2
    print(min(ans))
    





