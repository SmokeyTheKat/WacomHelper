import os
import sys
import subprocess
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

argv = sys.argv
argc = len(argv)

#os.system("xinput set-prop 12 --type=float \"Coordinate Transformation Matrix\" width 0 left-margin 0 height top-margin 0 0 1"

if "-e" in argv:
	strxinputs = str(subprocess.run(["xinput"], stdout=subprocess.PIPE, text=True, input=""))
	xinputs = strxinputs.split("\\n")
	uid = "-1"
	if "-t" in argv:
		stype = argv[argv.index("-t")+1]
		for a in xinputs:
			if stype in a:
				uid = a.split("\\t")[1].split("=")[1]
	elif "-i" in argv:
		uid = argv[argv.index("-i")+1]

	width = argv[argv.index("-s")+1].split("x")[0]
	height = argv[argv.index("-s")+1].split("x")[1]
	lmargin = argv[argv.index("-m")+1].split("x")[0]
	rmargin = argv[argv.index("-m")+1].split("x")[1]
	
	os.system("xinput set-prop "+uid+" --type=float \"Coordinate Transformation Matrix\" "+width+" 0 "+lmargin+" 0 "+height+" "+rmargin+" 0 0 1")
	print("xinput set-prop "+uid+" --type=float \"Coordinate Transformation Matrix\" "+width+" 0 "+lmargin+" 0 "+height+" "+rmargin+" 0 0 1")
