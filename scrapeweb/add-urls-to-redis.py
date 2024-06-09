import os
import redis

# Create a redis client
username = os.environ.get('REDIS_USERNAME')
password = os.environ.get('REDIS_PASSWORD')
redis_connection_url = os.environ.get('REDIS_CONNECTION_URL')
redis_port_number = os.environ.get('REDIS_PORT_NUMBER')
redisClient = redis.from_url(f'redis://{username}:{password}@{redis_connection_url}:{redis_port_number}')

# Push URLs to Redis Queue
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/1/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/2/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/3/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/4/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/5/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/6/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/7/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/8/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/9/")
redisClient.lpush('quotes_queue:start_urls', "https://quotes.toscrape.com/page/10/")
