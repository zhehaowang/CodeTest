from HTMLParser import HTMLParser
import requests
import re

# Naive scraper that gets you Inside the Black Box: A Simple Guide to Quantitative and High-Frequency Trading, Second Edition from UCLA library; hard coded for now.

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.pdfLinks = dict()

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for attr in attrs:
				# print(attr)
				if (attr[0] == 'href'):
					if (attr[1] and attr[1].find(r"/pdf") != -1):
						self.pdfLinks[attr[1].split(".")[2].replace("/", ".")] = attr[1]
		return

	def handle_endtag(self, tag):
		return

	def handle_data(self, data):
		
		return

if __name__ == "__main__":
	hostName = 'http://onlinelibrary.wiley.com'
	finalName = hostName + '/book'
	page = requests.get(finalName + '/10.1002/9781118662717')
	
	# instantiate the parser and fed it some HTML
	parser = MyHTMLParser()
	parser.feed(page.text)

	for item in parser.pdfLinks:		
		url = hostName + parser.pdfLinks[item]
		print "Getting: " + url
		response = requests.get(url, stream = True)

		if "<iframe" in response.content and "</iframe>" in response.content:
			startIdx = response.content.find("<iframe")
			endIdx = response.content.find("</iframe>")

			m = re.search(r'<iframe id="pdfDocument" src="([^"]*)" .*', response.content[startIdx:endIdx])
			if m:
				print "Fetching: " + m.group(1)
				pdfUrl = requests.get(m.group(1))
				with open(item, 'wb') as f:
					for chunk in pdfUrl.iter_content(chunk_size = 1024): 
						if chunk: # filter out keep-alive new chunks
							f.write(chunk)
							f.flush()
			else:
				print "Unexpected: no match " + response.content[startIdx:endIdx]
		else:
			print "Unexpected: iframe not in redirect page"

		