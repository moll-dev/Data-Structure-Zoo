''' test.py

	For testing the Queue class

	thomas moll 2015
'''
import unittest, queue

class TestQueue(unittest.TestCase):
	def setUp(self):
		pass

	def test_enqueue(self):
		q = queue.Queue()

		item1, item2 = 'fish', 'chips'

		q.enqueue(item1)
		q.enqueue(item2)

		self.assertEquals(item1, q.peek())


	def test_dequeue(self):
		q = queue.Queue()

		item1, item2 = 'the tube', 'crumpets'

		q.enqueue(item1)
		q.enqueue(item2)

		self.assertEquals(item1, q.dequeue())

	def test_size(self):
		q = queue.Queue()

		item1, item2 = 'the queen', 'james bond'
		self.assertEqual(0, len(q))

		q.enqueue(item1)
		self.assertEqual(1, len(q))

		q.enqueue(item2)
		self.assertEqual(2, len(q))

		q.dequeue()
		self.assertEqual(1, len(q))

	def test_peek(self):
		q = queue.Queue()

		item1, item2 = 'bangers', 'and mash'

		q.enqueue(item1)
		q.enqueue(item2)

		self.assertEqual(item1, q.peek())

	def test_clear(self):
		q = queue.Queue()

		item1, item2 = 'rainy weather', 'island nation'

		q.enqueue(item1)
		q.enqueue(item2)

		q.clear()

		self.assertEqual(0, len(q))
		self.assertEqual(None, q.peek())

if __name__ == '__main__':
    unittest.main(verbosity=2)
