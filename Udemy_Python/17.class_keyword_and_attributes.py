# class Bird:

# 	def __init__(self,color,wingspan,residence):
# 		self.clr = color
# 		self.wngspn = wingspan
# 		self.res= residence


# bird = Bird(color=input("Color:"),wingspan=input("Wingspan: "),residence=input("residence: "))
# print(bird.wngspn)

class X:
    def __init__(self):
         self.a = 10
         self._b = 20
         self.b = 20
    def getB(self):
         return self.b

x = X()
x._b = 60
print(x.getB())