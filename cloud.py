#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import Counter
import urllib
import random
import webbrowser
from konlpy.utils import pprint
from konlpy.tag import Kkma
from lxml import html
import pytagcloud # requires Korean font support
import sys
import pickle 
if sys.version_info[0] >= 3:
    urlopen = urllib.request.urlopen
else:
    urlopen = urllib.urlopen


r = lambda: random.randint(0,255)
color = lambda: (r(), r(), r())

def reading(filename):
	with open(filename, 'rb') as fp: 
		l = pickle.load(fp);
	return l; 
	


def get_tags( string,ntags=200, multiplier=3):
    nouns = reading(string)
    pprint(nouns)
    count = Counter(nouns)
    return [{ 'color': color(), 'tag': n, 'size': int(2.3*c/4)}\
                for n, c in count.most_common(ntags)]

def draw_cloud(tags, filename, fontname='Noto Sans CJK', size=(800, 600)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
    webbrowser.open(filename)


tags = get_tags("bin/nouns")
print(tags)
draw_cloud(tags, 'wordcloud.png')

#tags = get_tags("bin/verbs")
#print(tags)
#draw_cloud(tags, 'wordcloud1.png')

#tags = get_tags("bin/eomi")
#print(tags)
#draw_cloud(tags, 'wordcloudEomi.png')
