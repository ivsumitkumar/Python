dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(dict['key1'])
print(dict.keys())   # to check the no. of keys and their names in dictionary
print(dict.values())     # to check the values in dictionary
print(dict.items())     # to check the keys and values in dictionary


print("\n#Update() and setdefault() methods")
l=[i for i in range(0,10)]
l.append(8)
l.append(8)
l.append(7)
l.append(2)
print(l)
d={}
for i in l:
	d.update({i:d.setdefault(i,0)+1})
print(d)
