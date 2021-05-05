file = open('file.txt', 'r')
repeatedword = ""
repeat = 0
li = []
for line in file:
    lineword = line.lower().replace(",", "").replace(",", "").split(" ")
    for w in lineword:
        li.append(w)
for i in range(0, len(li)):
    count = 1
    for j in range(i + 1, len(li)):
        if(li[i] == li[j]):  # finding count of each word
            count += 1
    if(count > repeat):
        repeat = count
        repeatedword = li[i]
print("Most Frequent word: " + repeatedword)
print("Frequency: " + str(repeat))
file.close()
