#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import sys

cityAliasDict={}
def dealMulColumnnoRept(filename):
	global cityAliasDict
	fp = open(filename,'r')
	for line in fp:
		line = line.strip()
		citylist = line.split('\t')
		cl_len=len(citylist)
		for i in range(cl_len):
			keywd=citylist[i]
			tmpset=set(citylist)
			tmpset.remove(keywd)
			if keywd in cityAliasDict:
				cityAliasDict[keywd]=cityAliasDict[keywd]|tmpset	
			else:
				cityAliasDict.setdefault(keywd,tmpset)
	fp.close()
	
	for keys in cityAliasDict:
		ll=''
		for i in cityAliasDict[keys]:
			ll=ll+'\t'+i
		print keys+'\t'+ll	
	
def dealTwoColwithRept(filename):
	global cityAliasDict
	
	fp = open(filename,'r')
	for line in fp:
		line =line.strip()
		try:
			city1,city2 = line.split('\t',1)
		except Exception,e:
			continue

		if city1==city2:
			continue

		if city1 in cityAliasDict:
			cityAliasDict[city1].add(city2)
		else:
			cityAliasDict.setdefault(city1,set([city2]))

		if city2 in cityAliasDict:
			cityAliasDict[city2].add(city1)
		else:
			cityAliasDict.setdefault(city2,set([city1]))
#	for keys in cityAliasDict:
#		for i in cityAliasDict[keys]:
#			print keys+'\t'+i

def dealdata(filename):
	global cityAliasDict
	fp = open(filename,'r')
	for line in fp:
		ll=''
		line =line.strip()
		docid,title=line.split('\t')
		title=title.strip()
		if title in cityAliasDict:
			for word in cityAliasDict[title]:
				ll= word + '{|||}'+ll
			print docid+'\t'+title+'\t'+ll
			
if __name__=='__main__':
	dealTwoColwithRept("cityalias.txt")
	dealMulColumnnoRept("chinaalias.txt")
	dealdata("tour8005")
