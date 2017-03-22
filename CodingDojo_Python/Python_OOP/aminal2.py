from animal import Animal

class Dog(Animal):
	def __init__(self, name, heath):
		super(Dog, self).__init__(self, name, health)
		self.health = 150

	def pet(self):
		self.health +=5
		return self

dog1 =(Animal)
dog1.walk().walk().walk().run().run().pet().displayHealth()