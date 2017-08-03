import requests
import urllib
import json
access_token='Your Access Token'
def get_page_data(page_id):
	url='https://graph.facebook.com/'+str(page_id)+'/feed?limit=20&access.token='+access_token
	# we can also use urllib instead of requests module
	'''
	data=urllib.urlopen(url).read()
	'''
	data=requests.get(url)
	response=json.loads(data.text)
	#Extrackts post id.
	post_id=response['data'][0]['id']
	print post_id
	#Url for extracting likes on the post.
	like_url='https://graph.facebook.com/'+str(post_id)+'/likes?limit=100&access_token='+access_token
	#It gives out the persons name and id who liked the perticular post.
	print requests.get(like_url).text
	#Remove the exit to make below code run.
	exit()
	#Prints all messages of posts.
	'''for post in response['data']:
		if 'message' not in post : continue
		print post['message']
		print "\n\n"'''
	print response
	# Code For extracting url to next page.
	next_page=response['paging']['next']
	while next_page:
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
get_page_data('1413735098927291')
