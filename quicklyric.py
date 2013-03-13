#! /usr/bin/env python
from __future__ import print_function
from bs4 import BeautifulSoup
import urllib2
import re

base_url = "http://www.lyrics.com/"
artist_name = raw_input('enter artist name\n')
Artist = artist_name.replace(' ','-')
song_name = raw_input('enter song name\n')
Song = song_name.replace(' ','-')
url = urllib2.urlopen((base_url) + Song + '-lyrics' + '-' + Artist + '.html').read()
lyricsoup = BeautifulSoup(url)
a = str(lyricsoup.find("div", id="lyric_space"))
b = a.replace('<br/>',' ')

print(b)
