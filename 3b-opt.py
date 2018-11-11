#!/usr/bin/python3
#3b-opt.py
#MoulesFrites
#11/11/2018
#Script de sauvegarde avec opt

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

def unAutre():

	saisi = input('Un autre ? (yes/no)')
	if saisi == 'no' :
		sys.exit(0)
	elif saisi == 'yes' :
		filepath = input("Entrez le dossier/fichier à compresser\n")
		existPath = os.path.exists(filepath)
		if existPath == True :
			main(filepath)
		else :
			sys.stdout.write('Error filePath/dirPath\n')
	else :
		sys.stdout.write("Erreur dans la matrice")

def main(filePath):

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
	unAutre()

if len(sys.argv) > 1 :
	opt1 = sys.argv[1]
	if opt1 == '-h' :
		sys.stdout.write('Vous avez demander de l\'aide ?\n')
	else :
		existPath = os.path.exists(opt1)
		if existPath == True :
                	main(opt1)
		else :
			sys.stdout.write('Error filePath/dirPath\n')
else :
	filepath = input("Entrez le dossier/fichier à compresser\n")
	existPath = os.path.exists(filepath)
	if existPath == True :
		main(filepath)
	else :
		sys.stdout.write('Error filePath/dirPath\n')
