#! /usr/bin/python3
# -*- coding: utf-8 -*-
import konlpy
import string
from konlpy.utils import pprint, concordance 
from konlpy.tag import Kkma 
from konlpy.tag import Mecab 
from konlpy.tag import Hannanum
from konlpy import utils
from collections import Counter

## For saving in a list
import pickle 

def saving(filename, l):
	with open("bin/"+filename, 'wb') as fp: 
		pickle.dump(l, fp);


def reading(filename):
	with open("bin/"+ filename, 'rb') as fp: 
		l = pickle.load(fp);
	return l; 


def grafico( l):
	cnt = Counter(l);
	draw_zipf(cnt.Values(), 'zipf.png');

def verbs( pos ): 
	l = [] 
	for i in pos: 
		if (i[1][0] == 'V'):
			a = i[0] + ("다")
			pprint(a)
			l.append((a,i[1]))
	return l;
	
def nouns( pos ): 
	l = [] 
	for i in pos: 
		if (i[1][0] == 'N'):
			l.append(i)
	return l;
	
def verbs( pos ): 
	l = [] 
	for i in pos: 
		if (i[1][0] == 'V'):
			a = i[0] + ("다")
			pprint(a)
			l.append((a,i[1]))
	return l;

def adverbs( pos ): 
	l = [] 
	for i in pos: 
		if (i[1][0] == 'M'):
			l.append(i)
	return l;
	
def nouns( pos ): 
	l = [] 
	for i in pos: 
		if (i[1][0] == 'N'):
			l.append(i)
	return l;

def eomi( pos ): 
	l = [] 
	for i in pos: 
		if (i[1][0] == 'E'):
			l.append(i)
	return l;

def writetxt(file, l): 
	text_file = open(file, "w")
	st = '\n'.join(map(str,l))
	text_file.write(st)
	text_file.close()

def extractname(k):
	l = [] 
	for i in k: 
		l.append(i[0])
	return l;


doc = utils.read_txt("corpus/TOPIKCORPUS.txt", encoding=u'utf-8');


pos = []
#nouns = Kkma().nouns(doc);
pos = Kkma().pos(doc);
#nouns = reading("nouns");
#pos = reading("pos");
saving("pos", pos);


pprint(pos[1][1][0])


v = verbs(pos)
cntv = Counter(v);
pprint(cntv)
writetxt("verbs.txt",cntv.most_common())

v =  extractname(v)
saving("verbs",v);


nounss = nouns(pos)
cntn = Counter(nounss);
pprint(cntn.most_common(30))

writetxt("Nouns.txt",cntn.most_common())

nounss =  extractname(nounss)
saving("nouns",nounss);

adverbs = adverbs(pos)
cnta = Counter(adverbs);
#pprint(cnta)

writetxt("adverbs.txt",cnta.most_common())


e = eomi(pos)
cnte = Counter(e);
pprint(cnte.most_common(30))

writetxt("Eomi.txt",cnte.most_common())

e =  extractname(e)
saving("eomi",e);
