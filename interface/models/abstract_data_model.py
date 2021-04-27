from abc import ABCMeta


class AbstractDataModel(metaclass=ABCMeta):

	def __init__(self, *args, **kwargs):
		pass
	
	@staticmethod
	def json():
		raise NotImplemented
