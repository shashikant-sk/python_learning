class DEFAULT:
    
	# default constructor
	def __init__(self):
		self.geek = "DEFAULT"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = DEFAULT()

# calling the instance method using the object obj
obj.print_Geek()
