#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import sys

#cityAliasDict={}
cityLabelDict={}
label = 0
titleSet=set()
labelDict={}

def forTitleSet(filename):
	global titleSet
	fp=open(filename,'r')
	for line in fp:
		line = line.strip()
		try:
			docid,title=line.split('\t')
			title=title.strip()
			titleSet.add(title)
		except Exception,e:
			continue
	fp.close()
	
	
def dealMulColumnnoRept(filename):
	global cityLabelDict,label,titleSet
	fp = open(filename,'r')
	for line in fp:
		line = line.strip()
		citylist = line.split('\t')
		cl_len=len(citylist)
		if citylist[0] in cityLabelDict:
			pass
		else:
			cityLabelDict.setdefault(citylist[0],set([label]))
			label=label+1
		for i in range(1,cl_len):
			if citylist[i] in cityLabelDict:
				cityLabelDict[citylist[i]]=cityLabelDict[citylist[i]]|cityLabelDict[citylist[0]]
			else:
				cityLabelDict.setdefault(citylist[i],cityLabelDict[citylist[0]])
			
	fp.close()
	
#	for city in cityLabelDict:
#		ll=''
#		for i in cityLabelDict[city]:
#			ll=ll+' '+str(i)
#		print city+'\t'+ll	
	
def dealTwoColwithRept(filename):
	global cityLabelDict,label,titleSet
	
	fp = open(filename,'r')
	for line in fp:
		line =line.strip()
		try:
			city1,city2 = line.split('\t')
		except Exception,e:
			continue
		city1=city1.strip()
		city2=city2.strip()

		if city1==city2:#avoid the data mistake
			continue

		if city1 in cityLabelDict:
			pass
		else:
			cityLabelDict.setdefault(city1,set([label]))
			label=label+1
			
		if city2 in cityLabelDict:
			cityLabelDict[city2]=cityLabelDict[city1]|cityLabelDict[city2]
		else:
			cityLabelDict.setdefault(city2,cityLabelDict[city1])

	fp.close()
#	for city in cityLabelDict:
#		ll=''
#		for i in cityLabelDict[city]:
#			ll=ll+' '+str(i)
#		print city+'\t'+ll
			
def setupLabelDict():
	global cityLabelDict,labelDict
	for city in cityLabelDict:
		for label in cityLabelDict[city]:
			if label in labelDict:
				labelDict[label].add(city)
			else:
				labelDict.setdefault(label,set([city]))

def execute(filename):
	global cityLabelDict,labelDict,titleDict
	fp = open(filename,'r')
	for line in fp:
		line = line.strip()
		try:
			docid,title = line.split('\t')
			tmpset=set()
			for number in cityLabelDict[title]:
				tmpset=tmpset|labelDict[number]
			tmpset.remove(title)
			ll=''
			for citys in tmpset:
				ll=ll+'{|||}'+citys
			ll=ll.strip('{|||}')
			print docid+'\t'+title+'\t'+ll
		except Exception,e:
			continue	
	fp.close()

			
if __name__=='__main__':
	forTitleSet("tour8005")
	forTitleSet("tour8002")
	dealTwoColwithRept("cityalias.txt")
	dealMulColumnnoRept("chinaalias.txt")
	setupLabelDict()
	execute("tour8002")
	execute("tour8005")
