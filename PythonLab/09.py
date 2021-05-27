arr=[1,2,3,4,5,6,7,8,9,10]
n=len(arr)
key=int(input("Enter the number to be searched: "))
l=0
u=n-1
mid=(u+l)//2
while(l<=u):
    if(key==arr[mid]):
        print("found at index",mid)
        break
    elif(key>arr[mid]):
        l=mid+1
    elif(key<arr[mid]):
        u=mid-1
    mid=(l+u)//2
else:
    print("not found")