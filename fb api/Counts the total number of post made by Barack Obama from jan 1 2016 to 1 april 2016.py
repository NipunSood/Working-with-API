import requests
import urllib
import json
access_token='YOUR TOKEN'
def get_page_data(page_id):
	count=0
	next_page='https://graph.facebook.com/'+str(page_id)+'/feed?limit=100&access.token='+access_token
	data=requests.get(next_page)
	response=json.loads(data.text)
	#Prints all messages of posts.
	while next_page:
		for post in response['data']:
			if post['created_time'][3]=='6' and post['created_time'][6]<='4':	
				if post['created_time'][6]=='4':
					if post['created_time'][8]=='0' and post['created_time'][9]=='1':
						count+=1
					else:continue
				else:
					count+=1
		if 'paging' in response:
			if 'next' in response['paging']:
				next_page=response['paging']['next']
				next_page=next_page+'&access.token='+access_token
				response=json.loads(requests.get(next_page).text)
			else:
				next_page=None
		else:
			next_page=None
	print count
# 6815........ is the page id
get_page_data('6815841748')
