#!/usr/bin/python3
#1c-moy.py
#MoulesFrites
#16/10/2018
#Tri par ordre numerique les note avec les noms qui lui sont associé, fais un top5 de ces derniers
import operator

stringInput = ""
noteInput = 0
dictbase = {}
print("Entrez les noms puis la note et terminez par \"q\" : ")
while stringInput != "q" :
	stringInput = input("Nom : ")
	noteInput = input("Note : ")
	if stringInput != "q" :
		dictbase[stringInput] = int(noteInput)
dictsort = sorted(dictbase.items(), key=operator.itemgetter(1),reverse = True)
print ("Le top 5 : ")
top5 = dictsort[:5]
pos = 1
for stringInput,noteInput in top5:
	print( "{0} - {1}, sa note : {2}".format(pos,stringInput,noteInput))
	pos += 1

