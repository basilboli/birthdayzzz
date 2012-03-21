# -*- coding: utf-8 -*-
# Writen by Vasyl Vaskul <basilboli@gmail.com>
# Illegal copying of this code prohibited by real patsan's law! (as said by @bobuk)

import httplib, urllib
import re
import simplejson as json
from datetime import datetime,date
import random
import sys

TOKEN='YOUR_TOKEN'
ALL_FRIENDS_URL='https://graph.facebook.com/YOUR_ID/friends?fields=name,birthday&access_token='+TOKEN
FRIEND_WALL_URL='graph.facebook.com'
BIRTHDAYS_LIMIT=5

def happy_birthday():
	congratulations_list = get_today_birthdays()
	send_congrats (congratulations_list)	

def get_today_birthdays ():
	birthdays_today=[]
	friends= urllib.urlopen(ALL_FRIENDS_URL).read()
	items = json.loads(friends).get('data')
	for item in items:
		birthday=item.get('birthday')
		if birthday and is_today(birthday):#if person shares its birthday AND it's today
			birthdays_today.append(item)
	print "today:", birthdays_today
	return birthdays_today	 
	
def send_congrats (persons):
	count = 0
	params = urllib.urlencode({'access_token': TOKEN,'message': get_random_message()})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPSConnection(FRIEND_WALL_URL)

	for person in persons:
		if count > BIRTHDAYS_LIMIT: # foolproof feature
			return
		URL = "/%s/feed" %person.get('id')		
		conn.request("POST", URL, params, headers)
		response = conn.getresponse()
		data = response.read()
		print URL, response.status, response.reason, data
		count=count+1

	conn.close()
	print "%d persons congratulated!" %count				

def is_today (str):
	if not str:
		return False 

	today = date.today()	
	if len(re.split('/',str))==2:#checking format of the date
		dt = datetime.strptime(str, "%m/%d")
	elif len(re.split('/',str))==3:
		dt = datetime.strptime(str, "%m/%d/%Y")
	else:
		return False
			
	if today.day==dt.day and today.month==dt.month: 
		return True
	else: 
		return False	

def get_random_message():
	messages = open('texts','r').readlines()
	line_no = random.randint(1,len(messages)-1)
	print "choosing phrase...",messages[line_no] 
	return messages[line_no]
		
if __name__ == "__main__":
	#happy_birthday()
	get_today_birthdays()
	
	
