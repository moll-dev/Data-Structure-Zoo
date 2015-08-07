import unittest 
import objects

class TestObjectMethods(unittest.TestCase): 

	def test_vehicle(self): 
		self.vehicle = objects.Vehicle('Broken Skateboard')
		self.assertEqual(self.vehicle.name, 'Broken Skateboard')
		with self.assertRaises(NotImplementedError): 
			self.vehicle.vroom()
	 	with self.assertRaises(ValueError): 
	 		self.vehicle.name = 'foo'

	def test_car(self): 
		self.car = objects.Car('Saturn Ion') #RIP Saturn
		self.assertEqual(self.car.name, 'Saturn Ion')
		self.assertEqual(self.car.number_of_wheels, 4)
		self.assertEqual(self.car.vroom(), "Put Put Put")
		with self.assertRaises(ValueError): 
	 		self.car.name = 'bar'
		

	def test_truck(self): 
		self.truck = objects.Truck('Walmart Truck')
		self.assertEqual(self.truck.name, 'Walmart Truck')
		self.assertEqual(self.truck.number_of_wheels, 18)
		self.assertEqual(self.truck.vroom(), 'Vroooooom')
		with self.assertRaises(ValueError): 
	 		self.truck.name = 'baz'
		

if __name__ == '__main__':
    unittest.main()