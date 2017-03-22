class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = 100


	def walk(self):
		self.health -=1
		return self

	def run(self):
		self.health -=5
		return self

	def displayHealth(self):
		print self.name, self.health
		return self

animal1= (Animal)
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name, heath):
		super(Dog, self).__init__(self, name, health)
		self.health = 150

	def pet(self):
		self.health +=5
		return self

dog1 =(Animal)
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Dog):
	def __init__(self, nane, heatlh):
		super(Dragon, self).__init__(self, name, health)
		self.health = 170

	def fly(self):
		self.health -=10
		print ("This is a dragon!")
		return self

dragon1 =(Dog)
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
