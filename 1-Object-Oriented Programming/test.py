import unittest 
import objects

class TestObjectMethods(unittest.TestCase): 
	#ummmm maybe I don't need to set up for these tests since they're three different vehicles
	# def setup(self): 
	# 	self.car = Car('Tesla')
	# 	self.truck = Truck('')

	def test_vehicle(self): 
		pass

	def test_car(self): 
		print("Running 'Car' Tests!")
		self.car = objects.Car('Saturn Ion') #RIP Saturn
		self.assertEqual(self.car.name, 'Saturn Ion')
		self.assertEqual(self.car.number_of_wheels, 4)
		self.assertEqual(self.car.vroom(), "Put Put Put")

	def test_truck(self): 
		print("Running 'Truck' Tests!")
		self.truck = objects.Truck('Walmart Truck')
		self.assertEqual(self.truck.name, 'Walmart Truck')
		self.assertEqual(self.truck.number_of_wheels, 18)
		self.assertEqual(self.truck.vroom(), 'Vroooooom')
		pass

if __name__ == '__main__':
    unittest.main()