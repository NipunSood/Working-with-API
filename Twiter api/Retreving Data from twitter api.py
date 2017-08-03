from twython import Twython
import json
APP_KEY=''
App_SECRET=''
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET=''
twitter=Twython(APP_KEY,App_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
data=twitter.search(q='#election2016',result_type='mixed',count=10)
statuses=data['statuses']
for post in statuses:
	print post['id_str']+":"+post['text']
#print timeline
