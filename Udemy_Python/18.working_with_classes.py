class Rectangle:

	type= "Quadrilateral"		#"type" is class attribute

	def __init__(self,length,breadth):
		self.length= length
		self.breadth= breadth
		# self.area= self.length*self.breadth
		# self.perimeter= 2*(self.length+self.breadth)
		# self.update= (length=int(input("Enter New length: ")),breadth=int(input("Enter New breath: ")))

	def area(self):
		return self.length*self.breadth

	def perimeter(self):
		return 2*(self.length+self.breadth)

	def update(self,new_length,new_breadth):
		self.length= new_length
		self.breadth= new_breadth
		self.ar= self.length*self.breadth
		self.pr= 2*(self.length+self.breadth)

rect= Rectangle(length=int(input("Length: ")),breadth=int(input("Breadth: ")))
a= rect.area()
p= rect.perimeter()
 
print("Area is",a)
print("Perimeter is",p)
print("Type is",Rectangle.type)

while True:
	x= int(input("1.Edit Parameters\n2.Exit\n"))
	if x==1:
		rect.update(int(input("New length: ")),int(input("New breadth: ")))
		print("Area is:",rect.ar)
		print("Perimeter is:",rect.pr)
	elif x==2:
		print("Exiting...")
		break;
	else:
		print("Invalid choice!")

