#python
import urllib.request
import json

#query all courses
url = u'https://api.metalab.csun.edu/curriculum/api/2.0/courses'

#try to read the data	
try:
   u = urllib.request.urlopen(url)
   data = u.read()
except Exception as e:
	data = {}

#decode into an array
data = json.loads(data)

#setup a blank array
course_list = []

#loop through results and add each course's subject
#and catalog number to course_list array (i.e COMP 100)
for course in data['courses']:
   if(course['subject'] not in course_list):
	   course_list.append(course['subject'])
with open('abbrv.json','w') as json_file:
   json.dump(course_list,json_file)