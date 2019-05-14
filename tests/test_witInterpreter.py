from unittest import TestCase

from rasa_wit.interperter import WitInterpreter
from random import choice

token = '<your-token>'

#this is not exactly unit test - I know

class TestWitInterpreter(TestCase):
	def test_parse(self):
		interpreter = WitInterpreter(token)
		queries = ['hi','no intent for this one','hello']
		response = interpreter.parse(choice(queries))
		print(response)

		self.addTypeEqualityFunc(type(response),dict)
