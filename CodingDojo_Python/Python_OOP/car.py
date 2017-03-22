class Car(object):
	def __init__(self, price, speed, feul, mileage):
		self.price = price
		self.speed = speed
		self.feul = feul
		self.mileage = mileage
		

	def tax(self):
		self.tax = tax
		if price>10000:
			tax = 0.15
		else:
			tax = 0.12

	def display_all(self):
		print "Price", self.price
		print "Speed", self.speed
		print "Feul", self.feul
		print "mileage", self.mileage
		print "tax", self.tax

car1 = Car(2000, "35mph", "Full", "15mph")
car2 = Car(3000, "30mph", "3/4", "15mph")
car3 = Car(4000, "28mph", "1/2", "15mph")
car4 = Car(5000, "25mph", "1/4", "15mph")
car5 = Car(10000, "33mph", "1/8", "15mph")
car6 = Car(8000, "28mph", "Empty", "15mph")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()

