import os, pyshorteners

def xxx():
	os.system ("clear")
	try:
		link = input("\033[1;97m- enter url : ")
		shortener = pyshorteners.Shortener()
		text = shortener.tinyurl.short(link)
		print("\033[1;97m- hasil short url : "+text)
	except:
		exit()
    
    
xxx()