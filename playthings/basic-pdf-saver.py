from HTMLParser import HTMLParser
import requests

# Naive scraper that gets you Types and Programming Languages pdf from UCLA library; hard coded for now.

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.pdfLinks = dict()
		self.readyForLastName = False
		self.lastName = ""
		self.startIndex = 0

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for attr in attrs:
				print(attr)
				if (attr[0] == 'href'):
					if (attr[1] and attr[1].find(r"articleDetails.jsp") != -1):
						self.readyForLastName = True
					if (attr[1] and attr[1].find(r".pdf") != -1 and self.lastName != ""):
						self.pdfLinks[self.lastName] = attr[1]
						self.lastName = ''
		return

	def handle_endtag(self, tag):
		return

	def handle_data(self, data):
		if self.readyForLastName:
			self.lastName = data.lower().strip().replace(' ', '-').replace(',', '')
			if (self.lastName != ''):
				self.lastName = str(self.startIndex) + '-' + self.lastName
				self.startIndex += 1
		self.readyForLastName = False

		return

if __name__ == "__main__":
	hostName = 'http://ieeexplore.ieee.org'
	finalName = hostName + '/ebooks'
	page = requests.get(hostName + '/xpl/bkabstractplus.jsp?bkn=6267321')
	
	# instantiate the parser and fed it some HTML
	parser = MyHTMLParser()
	parser.feed(page.text)

	for item in parser.pdfLinks:
		strs = (hostName + parser.pdfLinks[item]).split('?')[1].split('&')
		attrs = dict()
		for attr in strs:
			attrs[attr.split('=')[0]] = attr.split('=')[1]
		url = finalName + '/' + attrs['bkn'] + '/' + attrs['fileName'] + '?bkn=' + attrs['bkn'] + '&pdfType=' + attrs['pdfType']
		
		response = requests.get(url, stream = True)
		with open(item + ".pdf", 'wb') as f:
			for chunk in response.iter_content(chunk_size = 1024): 
				if chunk: # filter out keep-alive new chunks
					f.write(chunk)
					f.flush()
