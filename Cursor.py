#include:utf-8
"""
Author : Horairy Hakim
email : hakim.horairy@telecom-sudparis.eu
Tel : 07 69 22 52 55
"""

class Cursor:

	def __init__(self, frame):

		self.frameID = frame.frameID
		self.indexLink = frame.metaData["linkCursor"]


