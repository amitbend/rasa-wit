from unittest import TestCase

from app import WitInterpreter
from random import choice

# token = '<your-token>'
token = '6ZSNEXDJIX2LVAZNQKGBBY6FVBIGQHPR'


class TestWitInterpreter(TestCase):
	def test_parse(self):
		interpreter = WitInterpreter(token)
		queries = ['hi','no intent for this one','hello']
		response = interpreter.parse(choice(queries))
		print(response)

		self.addTypeEqualityFunc(type(response),dict)
