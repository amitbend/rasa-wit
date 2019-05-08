from unittest import TestCase

from app import WitInterpreter
from random import choice

class TestWitInterpreter(TestCase):
	def test_parse(self):
		token = '6ZSNEXDJIX2LVAZNQKGBBY6FVBIGQHPR'
		interpreter = WitInterpreter(token)
		queries = ['fff']
		response = interpreter.parse(choice(queries))
		print(response)

		self.addTypeEqualityFunc(response,dict)
