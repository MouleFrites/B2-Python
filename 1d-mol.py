#!/usr/bin/python3
#1d-mol.py
#MoulesFrites
#23/10/2018
#Jeu du plus ou moins

import random
import signal
import sys
from time import sleep

def exitproperly(sig, frame):
    print('\nGood bye misteuuuuuur')
    sys.exit(0)

signal.signal(signal.SIGINT, exitproperly)

nbraleatoire = random.randint(0, 100)
nbrsaisi = 0
while nbrsaisi != nbraleatoire :
    nbrsaisi = int(input("Entrez un nombre : "))
    if nbrsaisi == nbraleatoire :
        break
    elif nbrsaisi >= nbraleatoire :
        mess = "C'est moins"
    elif nbrsaisi <= nbraleatoire :
        mess ="C'est plus"
    else :
        mess ="Erreur dans la matrice"
    print(mess)
print("Vous avez gagner, la solution etais : " + str(nbraleatoire))
