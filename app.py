import logging

from rasa_core.interpreter import RegexInterpreter
from wit import Wit

logger = logging.getLogger(__name__)


def build_entity(key, value):
	"""
	build_entity return a dict that can be passed back to rasa as an entity
	using the given string key and value
	"""
	return {"entity": key, "value": value, "start": 0, "end": 0}


def build_response(msg, intent=None, entities=None):
	"""
	build_response builds a rasa_core compatible dict using
	the given message, intent and list of entities
	"""
	out_entities = []
	if entities is not None:
		out_entities = [
			build_entity(key, value) for (key, value) in entities.items() if value
		]
	print('out',out_entities)
	return {"text": msg, "intent": intent if intent else {}, "entities": out_entities}


class UpstreamError(Exception):
	pass


class WitInterpreter(RegexInterpreter):
	"""
	DialogflowInterpreter is an Interpreter for use in rasa_core that
	performs Natural Language processing using dialogflow API v2
	"""

	def __init__(
		self,
		access_token,
		timezone="Africa/Nairobi",
		language_code="en",
		raise_on_error=False,
		flip_text_and_intent=False,
	):

		self.language_code = language_code
		self.raise_on_error = raise_on_error
		self.flip_text_and_intent = flip_text_and_intent
		self.timezone = timezone
		self.session_client = Wit(access_token=access_token)

	def parse(self, text):
		"""
		parse takes a string and responds with the NLU results sent
		by Wit
		"""
		context = {}
		if self.timezone:
			context['timezone'] = self.timezone

		try:
			response = self.session_client.message(text,context=context)
			print('raw response',response,type(response))
		except Exception as e:
			if self.raise_on_error:
				raise UpstreamError(str(e))
			else:
				logger.error(
					"Failed to parse text '{}' using Wit "
					"Error: {}".format(text, e)
				)
				return build_response(text)
		entities = response['entities']
		try:
			intent_raw = entities.pop('intent')[0]
			intent = {
				"name": intent_raw['value'],
				"confidence": intent_raw['confidence'],
			}

		except KeyError:
			intent = None

		return build_response(
			response['_text'],
			intent=intent,
			entities=entities,
		)
