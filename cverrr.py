import urllib2
import xmltodict
import pprint

feed = urllib2.urlopen('http://nvd.nist.gov/download/nvd-rss.xml')
data = feed.read()
feed.close()

doc = xmltodict.parse(data)

def cve():
  file = open('cve.html','w')
  file.write('<html>')
  for item in doc['rdf:RDF']['item']:
    file.write('<a href=' + item['link'] + '>' + '<b>' + item['title'] + '</b>'  + '</a>\n')
    file.write(item['description'] + '<p>')
  file.write('</html>')
  file.close()
  return()

cve()
#contents = str(content)

#f = open('cve.html', 'w')
#f.seek(0)
#f.write(contents)
#f.close()


#print '<html>'
#for url in doc['rdf:RDF']['channel']['items']['rdf:Seq']['rdf:li']:
#  print '<a href=' + url['@rdf:resource'] + '>' + url['@rdf:resource'] + '</a><p>'
#print '</html>'

