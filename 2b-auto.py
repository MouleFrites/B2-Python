#!/usr/bin/python3
#2b-mol.py
#MoulesFrites
#06/11/2018
#Solveur du Jeu du plus ou moins dans un fichier separer

import random
import signal
import sys
import time

def exitproperly(sig, frame):
	print('\nGood bye misteuuuuuur')
	sys.exit(0)

signal.signal(signal.SIGINT, exitproperly)
global readFile
readFile = None
global fileInfo
fileInfo = None
global randToTest
randToTest = 50
def actionOnFile(message, filePath, type):
	fichier = open(filePath, type)
	if type == "w" or type == "a" :
		fichier.write(str(message))
	elif type == "r" :
		readFile = fichier.read()
		return readFile
	else :
		print("Erreur actionOnFile")
	fichier.close()

def waitEventFile():
	startFile = actionOnFile(" ", cheminfichier, "r")
	waitFile = startFile
	while startFile == waitFile :
		waitFile = actionOnFile(" ", cheminfichier, "r")
		time.sleep(0.1)
	changedFile = waitFile

def goodNumberOrNot():
	print(fileInfo)
	global minToTest
	global maxToTest
	if fileInfo == "C'est plus" :
		minToTest = randToTest
	if fileInfo == "C'est moins" :
		maxToTest = randToTest
	return random.randint(minToTest, maxToTest)


cheminfichier = input("Entrez le chemin du fichier a lire\n")
fileInfo = actionOnFile(" ", cheminfichier, "r")
if fileInfo == "Yo aventurier" :
	minToTest = 0
	maxToTest = 100
	actionOnFile(randToTest, cheminfichier, "w")
	waitEventFile()
	fileInfo = actionOnFile(" ", cheminfichier, "r")
	while readFile != "Win" :
		fileInfo = actionOnFile(" ", cheminfichier, "r")
		if readFile == "Win" :
			print("Gagné!" )
			break
		else :
			randToTest = goodNumberOrNot()
			actionOnFile(randToTest, cheminfichier, "w")
		waitEventFile()
else :
	print("Redemarre l'autre python boulet")
print("C'est gagné !!")
