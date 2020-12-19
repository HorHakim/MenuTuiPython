#include:utf-8
"""
Author : Horairy Hakim
email : hakim.horairy@telecom-sudparis.eu
Tel : 07 69 22 52 55
"""
from Frame import *
# from Cursor import *

frame = Frame(frameID=1)

while True :
	frame.ShowGraphicalGrid()
	frame.command()
	frame.ShowGraphicalGrid()