import unittest 
import objects

class TestObjectMethods(unittest.TestCase): 
	#ummmm maybe I don't need to set up for these tests since they're three different vehicles
	def setup(self): 
		self.car = Car('Tesla')
		self.truck = Truck('')

	def test_vehicle(self): 
		pass 

	def test_car(self): 
		pass 

	def test_truck(self): 
		pass


if __name__ == '__main__':
    unittest.main()