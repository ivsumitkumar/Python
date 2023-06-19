def cube(num):
    return num**3

print(cube(4))

        ###map(function,iterable)###
list1= [1,3,5,8,45,12]
result=list(map(cube,list1))
print(result,list1)

for i in map(cube,list1):
    print(i)


            ####filter(fuction,iterable)####
def even(num):
    return num%2==0

list2=[256,784,111,151,32]
print(list(filter(even,list2)))