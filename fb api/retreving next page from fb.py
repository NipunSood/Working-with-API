import requests
import urllib
import json
access_token='Your Access Token'
def get_page_data(page_id):
	count=0
	url='https://graph.facebook.com/'+str(page_id)+'/feed?limit=100&access.token='+access_token
	data=requests.get(url)
	response=json.loads(data.text)
	#Prints all messages of posts.
	for post in response['data']:
		count+=1
		print post['created_time']
		print "\n\n"
	print count
	next_page=response['paging']['next']
	while next_page:
		next_page=next_page+'&access.token='+access_token
		print next_page
		print "Found next page"
		response=json.loads(requests.get(next_page).text)
		if 'paging' in response:
			if 'next' in response['paging']:
				next_page=response['paging']['next']
			else:
				print "Next not found."
				next_page=None
		else:
			print "paging not found."
			next_page=None
get_page_data('6815841748')
