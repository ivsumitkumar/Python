with open("myfile.txt", "w") as f:
    f.write("Hello World Python Programming")

with open('myfile.txt', 'w+') as f:
    f.write("sparsh")
    f.seek(0)
    data = f.readlines()
    for line in data:
        words = line.split()
        print(words)
