arr=[1,2,3,4,5,6,7,8,9,10]
key=int(input("Enter number to search:"))
for i in range(len(arr)):
    if(key==arr[i]):
        print("found at index",i)
        break
else:
    print("Not found")