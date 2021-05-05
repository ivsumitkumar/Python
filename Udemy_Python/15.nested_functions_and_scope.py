#GLobal
x = 100

#Enclosing Function
def sample(x):
	x= 50

	#Local Scope
	def cube():
		print("In Local Scope x is :",x**3)

	cube()

	print("In Enclosing Function x is:",x)
	
sample(x)
print("In Global Scope x is :",x)


'''L: Local scope
E: Enclosing Function
G: Global scope
B: Built in'''