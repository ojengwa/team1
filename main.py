from BeautifulSoup import BeautifulSoup
import urllib2
def get_url(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)

	return soup


	#for link in soup.findAll('title'):
	#	print link.get()

get_url("http://andela.co")