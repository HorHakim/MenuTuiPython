#include:utf-8
"""
Author : Horairy Hakim
email : hakim.horairy@telecom-sudparis.eu
Tel : 07 69 22 52 55
"""
import json


def initiateFileConfig():
	
	metadataFrame = dict()
	metadataFrame["links"] = dict()
	metadataFrame["buttons"] = dict()

	return metadataFrame

def startConfiguringProjet(pathProject):

	metadataFrame = initiateFileConfig()
	
	print("Bienvenue dans le créateur de frame ! ")
	numberFrames = int(input("Combien de Frames voulez-vous créer ? "))

	print("\n")

	for idFrame in range(numberFrames):
		print("Nous allons maintenant créer la frame id : {0}".format(idFrame))
		print("\n")

		numberLinks = int(input("Combien de lien voulez-vous créer ? "))

		for indexLink in range(numberLinks):
			print("Lien n°{0} : ".format(indexLink))
			
			linkId = int(input("Quel est l'id de la frame que voulez-vous associer à ce lien ? "))
			linkName = input("Que voulez-vous afficher sur ce lien ? ")
			
			metadataFrame["links"][str(indexLink)] = [linkId, linkName]
			
			print("\n")


		numberButtons = int(input("Combien de buttons vous-voulez créer ? "))

		for indexButton in range(numberButtons):
			print("Button n°{0} : ".format(indexButton))
			buttonChar = input("Quel button voulez-vous associer à  ce button ? ")
			buttonName = input("Quel description vouslez-vous donnez à ce button ?")

			metadataFrame["buttons"][str(indexButton)] = [buttonChar, buttonName]

			print("\n")
		
		with open("{0}/metadataFrameID{1}".format(pathProject, idFrame), 'w') as metadateFile:
			json.dump(metadataFrame, metadateFile, indent=4)


####################################################################################################################################################

pathProject = "Projects/"

startConfiguringProjet(pathProject)