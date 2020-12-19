#include:utf-8
"""
Author : Horairy Hakim
email : hakim.horairy@telecom-sudparis.eu
Tel : 07 69 22 52 55
"""
import numpy
import os


class Frame:

	def __init__(self, numberLinksToFrames, numberButtons=None):

		self.numberLinksToFrames = numberLinksToFrames
		self.numberButtons = numberButtons

		self.getTerminalSize()
		self.logicalGrid = self.generateLogicalGrid()
		self.graphicalGrid = self.generateGraphicalGrid()
################################################################################################################		
##############################                Meta-data Frame       ############################################
################################################################################################################
	
	""" Ici on va gérer les métadatas."""
	

################################################################################################################

################################################################################################################
###############################   				Logics 				############################################
################################################################################################################

	
	def getTerminalSize(self):
		"""Instantiate 2 attributes for the frame class : 
					The number of rows and columns of the frame"""
		rows, columns = os.popen('stty size', 'r').read().split()
		self.NumberLines = int(rows) - 4
		self.numberColumns = int(columns)

	def getTerminalCenterPosition(self):
		return [self.NumberLines//2, self.numberColumns//2]

	
	def generateEmptyLogicalGrid(self):
		
		emptyLogicalGrid = numpy.ones(shape=(self.NumberLines, self.numberColumns), dtype=int)
		emptyLogicalGrid[1:-1, 1:-1] = numpy.zeros(shape=(self.NumberLines-2, self.numberColumns-2), dtype=int)
		
		return emptyLogicalGrid


	def addLinksOnLogicalGrid(self, emptyLogicalGrid, position="center"):
			
			if position == "center":
				position = self.getTerminalCenterPosition()
				position[0] -= (self.numberLinksToFrames - 1)

				for indexLink in range(self.numberLinksToFrames):
					emptyLogicalGrid[position[0], position[1]] = 2
					position[0] += 2
				
				logicalGrid = emptyLogicalGrid	
				return logicalGrid

	def generateLogicalGrid(self):

		emptyLogicalGrid = self.generateEmptyLogicalGrid()
		logicalGrid = self.addLinksOnLogicalGrid(emptyLogicalGrid=emptyLogicalGrid)

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

	def ShowGraphicalGrid(self):
		
		os.system("clear")
		print(self.graphicalGrid)

		return None


##################################################################################################################
