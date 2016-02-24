# This file accept tweets stream and store data in redis as two categories: 
# clinton and trump

import json, redis

# Set up redis connections
pool_trump = redis.ConnectionPool(host='localhost', port=6379, db=0)
pool_clinton = redis.ConnectionPool(host='localhost', port=6379, db=1)
conn_trump = redis.Redis(connection_pool=pool_trump)
conn_clinton = redis.Redis(connection_pool=pool_clinton)


def add_tweet(data):
	try:
		# Decode json string from the result
		obj = json.loads(data)
		time = obj['created_at']
		print time
		text = obj['text']
		if 'donaldtrump' in text.lower():
			conn_trump.setex(time, 'trump', 60)
			print 'add tweet for trump'
		if 'hillaryclinton' in text.lower():
			conn_clinton.setex(time, 'clinton', 60)
			print 'add tweet for clinton'
	except ValueError:
		print e.errno
