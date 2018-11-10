#!/usr/bin/python3
#2a-mol.py
#MoulesFrites
#05/11/2018
#Jeu du plus ou moins dans un fichier separer

import random
import signal
import sys
import time

def exitproperly(sig, frame):
    print('\nGood bye misteuuuuuur')
    sys.exit(0)

signal.signal(signal.SIGINT, exitproperly)

nbraleatoire = random.randint(0, 100)
nbrsaisi = 0
cheminfichier = input("Entrez le chemin du fichier a lire\n")
fichier = open(cheminfichier, "w")
fichier.write("Yo aventurier")
fichier.close()
while nbraleatoire != nbrsaisi :
	fichier = open(cheminfichier, "r")
	testbase = fichier.read()
	fichier.close()
	testattente = testbase
	if nbrsaisi == nbraleatoire :
                break
	while testbase == testattente :
		fichier = open(cheminfichier, "r")
		testattente = fichier.read()
		fichier.close()
		time.sleep(0.1)
	fichier = open(cheminfichier, "r")
	nbrsaisi = int(fichier.read())
	fichier.close()
	if nbrsaisi == nbraleatoire :
		break
	elif nbrsaisi >= nbraleatoire :
    	    	mess = "C'est moins"
	elif nbrsaisi <= nbraleatoire :
    	    	mess ="C'est plus"
	else :
    	    	mess ="Erreur dans la matrice"
	fichier = open(cheminfichier, "w")
	fichier.write(mess)
	fichier.close()
	print(mess)
fichier = open(cheminfichier, "w")
fichier.write("Win")
fichier.close()
print("Vous avez gagner, la solution etais : " + str(nbraleatoire))
