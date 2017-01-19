#OO:class and example
class Car:
	#define general attribute
	#can be revalued among different example
	speed=0
	#define class's method
	#self reprensents general examp
	#distance is an arguement which shall be assign by later input
	def drive(self,distance):
		time=float(distance/self.speed)
		print time

car1=Car()
car1.speed=60.0
car1.drive(100.0)
car1.drive(200)

car2=Car()
car2.speed=150.0
car2.drive(100.0)
car2.drive(200.0)
