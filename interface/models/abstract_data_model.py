from typing import Dict
from abc import ABCMeta, abstractmethod


class AbstractDataModel(metaclass=ABCMeta):

	def __init__(self, *args, **kwargs):
		pass

	@staticmethod
	@abstractmethod
	def json(self) -> Dict:
		raise NotImplemented
	