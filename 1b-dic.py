#!/usr/bin/python3
#1b-dic.py
#MoulesFrites
#15/10/2018
#Trie par orde alphabetique les chaines de caractère envoyé par l'utilisateur
strInput = ""
strList = list()
print("Entrez les prenoms et terminez par \"q\" : ")
while strInput != "q" :
	strInput = input()
	if strInput != "q" :
		strList.append(strInput)
strList.sort()
print(strList)

