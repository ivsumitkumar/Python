# import sys
# len = len(sys.argv)
# k = 0
# list = []
# for i in range(1, len):
#     list.append(int(sys.argv[i]))
# max = list[0]
# for i in range(0, len - 1):
#     if list[i] > max:
#         max = list[i]
# print("maximum is", max)
'''**************************************************'''
# l=input("Enter Numbers:").split(" ")
# print(max(l))
'''**************************************************'''
import sys
print(max([int(i) for i in sys.argv[1::]]))
 