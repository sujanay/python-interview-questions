import urllib2
import json

url = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=pizza'

contents = urllib2.urlopen(url).read()
contents = json.loads(contents)
print(type(contents)) 