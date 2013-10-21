#!/usr/bin/python
import sys
import urllib
import autoProcessTV

if len(sys.argv) != 4:
    print "Wrong number of arguments - is this being called from rtorrent?"
    sys.exit()

filePath = "".join(sys.argv[1].replace("/download/", "/complete/").rpartition("/")[:2])
fileName = sys.argv[2]
fileLabel = urllib.unquote_plus(sys.argv[3])

if fileLabel == "tv/sickbeard":
	autoProcessTV.processEpisode(filePath, fileName)
