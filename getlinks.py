#!/usr/bin/env python
#L0VER IN MYANMAR
#Data : 26,4,2016

import sys
def getlinks():
	import mechanize
	br = mechanize.Browser()
	br.addheaders = [('User-agent', 'Firefox')]# You Can Add Other Headers :D
	br.set_handle_robots(False)
	if sys.argv[1][-1] != '/':
		sys.argv[1] = sys.argv[1]+'/'
	br.open(sys.argv[1])
	links_tmp = [sys.argv[1]]
	links = []
	for link in br.links():
		link = link.url
		if link in links:
			continue
		# if sys.argv[1] not in link:
		elif 'http' not in link:
			link = sys.argv[1]+link	
		links_tmp.append(link)
	for i in links_tmp:
		if i not in links:
			links.append(i)
	for t,i in enumerate(links):
		print  ' %s ) %s' % (t+1,i)
if __name__ == '__main__':
	if len(sys.argv) == 1:
		print "Usage : python %s http://www.example.com/" % sys.argv[0]
	elif sys.argv[1] != '':
		try:
			getlinks()
		except Exception,e:
			print "Error : ", e