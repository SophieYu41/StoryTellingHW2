# This file read data from redis and compute the rate of each stream
# Time window is set to be 60s.

import redis, json, time, sys

# set up redis connections
pool_trump = redis.ConnectionPool(host='localhost', port=6379, db=0)
pool_clinton = redis.ConnectionPool(host='localhost', port=6379, db=1)
conn_trump = redis.Redis(connection_pool=pool_trump)
conn_clinton = redis.Redis(connection_pool=pool_clinton)


def compute_avg():
	while True:
		# compute rate for Trump
		keys_trump= conn_trump.keys()
		rate_trump = len(keys_trump)

		# compute rate for Clinton
		keys_clinton= conn_clinton.keys()
		rate_clinton = len(keys_clinton)

		# send the rate to stdout
		print json.dumps({"time": time.strftime("%Y-%m-%d %H:%M:%S"), "rate_trump": rate_trump, "rate_clinton": rate_clinton})
		sys.stdout.flush()

		time.sleep(10)


compute_avg()