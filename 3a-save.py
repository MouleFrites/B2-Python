#!/usr/bin/python3
#3a-save.py
#MoulesFrites
#11/11/2018
#Script de sauvegarde

import signal
import sys
import time
import os
import tarfile


def exitproperly(sig, frame):
        sys.stdout.write('\nGood bye misteuuuuuur\n')
        sys.exit(0)

signal.signal(signal.SIGINT, exitproperly)


def addFileNewTargz(fileName, tarName):
	tz = tarfile.open(tarName, 'w:gz')
	tz.add(fileName)
	tz.close()

filePath = input("Entrez le dossier/fichier à compresser\n")
existPath = os.path.exists(filePath)
if existPath == True :
	directory = 'data/'
	existPath = os.path.exists('data/')
	if existPath == False :
		os.mkdir(directory)
	tarName = 'save' + filePath + str(time.time())
	addFileNewTargz(filePath, str(tarName))
	os.rename(str(tarName), directory + tarName)
	existPath = os.path.isfile(directory + tarName)
	if existPath == True :
		sys.stdout.write('C\'est tout bon\n')
	else :
		sys.stdout.write('Erreur dans la matrice\n')
else :
	sys.stdout.write('Error filePath/dirPath\n')
