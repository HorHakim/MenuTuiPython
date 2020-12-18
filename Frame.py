#include:utf-8
"""
Author : Horairy Hakim
email : hakim.horairy@telecom-sudparis.eu
Tel : 07 69 22 52 55
"""
import numpy
import os

class Frame:

	def __init__(self, numberOptions):

		self.numberOptions = numberOptions

		self.getTerminalSize()
		self.logicalGrid = self.generateEmptyLogicalGrid()
		self.graphicalGrid = self.generateGraphicalGrid()

################################################################################################################
###############################   				Logics 				############################################
################################################################################################################


	def getTerminalSize(self):
		
		rows, columns = os.popen('stty size', 'r').read().split()
		self.NumberLines = int(rows) - 4
		self.numberColumns = int(columns)

	
	def generateEmptyLogicalGrid(self):
		
		emptyLogicalGrid = numpy.ones(shape=(self.NumberLines, self.numberColumns), dtype=int)
		emptyLogicalGrid[1:-1, 1:-1] = numpy.zeros(shape=(self.NumberLines-2, self.numberColumns-2), dtype=int)
		
		return emptyLogicalGrid

##################################################################################################################


##################################################################################################################
##############################					Graphics			##############################################
################################################################################################################## 				
	
	def generateGraphicalGrid(self):

		listeCharacs = [" ", "O"]
		graphicalGrid = ""
		
		for logicLine in self.logicalGrid:
			for logicValue in logicLine:

				graphicalGrid += listeCharacs[logicValue]
			graphicalGrid += "\n"
		
		return graphicalGrid 

##################################################################################################################
