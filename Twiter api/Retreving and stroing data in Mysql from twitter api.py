from twython import TwythonStreamer
import MySQLdb as mysql
import json

APP_KEY=''
App_SECRET=''
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET=''

host='localhost'
user='root'
passwd='nick'
db='osndata'
'''Creates a MySQL connection and return the cursor'''
def create_connection():
	connection=mysql.connect(host,user,passwd,db)
	cursor=connection.cursor()
	return connection,cursor
'''Close the connection'''
def close_connection(cursor,connection):
	cursor.close()
	connection.commit()
	connection.close()

class MyStreamer(TwythonStreamer):
	def on_success(self,data):
		if 'text' in data:
			connection,cursor=create_connection()
			text=data['text'].encode('utf-8')
			print text
			query='''INSERT IGNORE into tweets (tweet_id,text) VALUES (%s,%s)'''
			cursor.execute(query,(data['id_str'],text))
			close_connection(cursor,connection)
	def on_error(self,status_code,data):
		print status_code
		pass
stream=MyStreamer(APP_KEY,App_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
stream.statuses.filter(track="election2016")
