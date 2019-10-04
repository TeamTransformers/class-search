#python
import json

url = u'https://api.metalab.csun.edu/curriculum/api/2.0/courses'

new_url = []
with open('src/python/abbrv.json') as abbrv:
   data = json.load(abbrv)
   for p in data:
      new_url.append(url+"/"+p)
with open('src/python/url.json','w') as new:
   json.dump(new_url,new)