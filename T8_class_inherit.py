#Highly notice!The constructor in class is __init__!
#Vehicle is superclass
class Vehicle:
	#function__init__ will initialize target variable automatically
	#as soon as the class is established
	#then you directly use v=class(arg) instead of v=class();v.attribute=sth
	#the speed in brackets mean the arguement awaiting input
	def __init__(self,speed):
		#the 1st speed mean call the input speed of the examp
		#the 2nd speed mean save the input value into a variable'speed' inside class 
		self.speed=speed

	def drive(self,distance):
		#I suppose self.blabla means call sth?
		#so in the function where distance belong use self.speed
		print'Need %fhour(s)'%(distance/self.speed)

#Vehicle in brackets mean Bicycle is sonclass of Vehicle
class Bicycle(Vehicle):
	#Bicycle has nothong special from super class so pass it
	pass

class Car(Vehicle):
	def __init__(self,speed,fuel):
		Vehicle.__init__(self,speed)
		#save arg into a variable need call,while merely calculate don't?(distance?)
		self.fuel=fuel

	def drive(self,distance):
		#inherit superclass's function and print line need xx hours
		Vehicle.drive(self,distance)
		#special from superclass,add one more line need xx fuel
		print 'Need %f fuels'%(distance*self.fuel)

#define b is a examp of Bicycle and input its special attribute value"speed"
b = Bicycle(15.0)
#Car has two attributes,two special input
c = Car(80.0,0.012)
#call the function
b.drive(100.0)
c.drive(100.0)
