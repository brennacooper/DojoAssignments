class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price 
		self.max_speed = max_speed
		self.miles = miles
		

	def displayInfo(self):
		print (self.price, self.max_speed, self.miles)
		return self

	def ride(self):
		self.miles +=10
		print ("Riding " , self.miles)
		return self

	def reverse(self):
		self.miles -=5
		print ("Reversing", self.miles)
		return self

bike1 =(Bike)(250, "25mph")
bike2 =(Bike)(200, "20mph")
bike3 =(Bike)(300, "30mph")

bike1.ride().ride().ride().reverse().displayInfo()


bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()








