import heapq
a=[2,1,4,3,5]
heapq.heapify(a)
print(a)
print(-1*heapq.heappop(a))
print(a)