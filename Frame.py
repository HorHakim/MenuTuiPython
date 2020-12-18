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
		self.logicalGrid = self.generateLogicalGrid()
		self.graphicalGrid = self.generateGraphicalGrid()

################################################################################################################
###############################   				Logics 				############################################
################################################################################################################

	
	def getTerminalSize(self):
		
		rows, columns = os.popen('stty size', 'r').read().split()
		self.NumberLines = int(rows) - 4
		self.numberColumns = int(columns)

	def getTerminalCenterPosition(self):
		return [self.NumberLines//2, self.numberColumns//2]

	
	def generateEmptyLogicalGrid(self):
		
		emptyLogicalGrid = numpy.ones(shape=(self.NumberLines, self.numberColumns), dtype=int)
		emptyLogicalGrid[1:-1, 1:-1] = numpy.zeros(shape=(self.NumberLines-2, self.numberColumns-2), dtype=int)
		
		return emptyLogicalGrid


	def addOptionOnLogicalGrid(self, emptyLogicalGrid, position="center"):
			
			if position == "center":
				position = self.getTerminalCenterPosition()
				position[0] -= (self.numberOptions - 1)

				for indexOption in range(self.numberOptions):
					emptyLogicalGrid[position[0], position[1]] = 2
					position[0] += 2
				
				logicalGrid = emptyLogicalGrid	
				return logicalGrid

	def generateLogicalGrid(self):

		emptyLogicalGrid = self.generateEmptyLogicalGrid()
		logicalGrid = self.addOptionOnLogicalGrid(emptyLogicalGrid=emptyLogicalGrid)

		return logicalGrid
		



##################################################################################################################


##################################################################################################################
##############################					Graphics			##############################################
################################################################################################################## 				
	
	def generateGraphicalGrid(self):

		listeCharacs = [" ", "O", "+"]
		graphicalGrid = ""
		
		for logicLine in self.logicalGrid:
			for logicValue in logicLine:

				graphicalGrid += listeCharacs[logicValue]
			graphicalGrid += "\n"
		
		return graphicalGrid 

##################################################################################################################
