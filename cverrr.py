import urllib2
import xmltodict
import pprint

feed = urllib2.urlopen('http://nvd.nist.gov/download/nvd-rss.xml')
data = feed.read()
feed.close()

doc = xmltodict.parse(data)

def cve():
  file = open('/var/www/cve/cve.html','w')
#  file.write('<div class="cve">')
  for item in doc['rdf:RDF']['item']:
    file.write('<div class="cve"><a href=' + item['link'] + '>' + '<h3>' + item['title'] + '</h3>'  + '</a>\n')
    file.write('<div class="desc">' + item['description'] + '<p></div></div>')
#  file.write('</div>')
  file.close()
  return()

cve()

