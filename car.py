class Car(object):
	"""docstring for ClassName"""
	def __init__(self, name="General",model="GM",type_="saloon"):
		#Return a car object whose name is Honda
		self.name= name
		self.model=model
		self.type_=type_
		self.num_of_doors=4
		self.num_of_wheels=4
		self.speed=0

		#Number of doors based on car type
		if self.name=="Porshe" or self.name=="Koenigsegg":
		   self.num_of_doors=2
			#Tthe car should have four wheels not unless its a trailer
		if self.type_=="trailer":
		   self.num_of_wheels=8

				#The car type should be saloon if its not a trailer
	def is_saloon(self):
		if self.type_!='saloon':
			return False
		return True
	def drive (self,car_speed):
		if car_speed==3:
			self.speed=1000
			return self
		elif car_speed==7:
			self.speed=77
	    	return self

				
					
						
					

		