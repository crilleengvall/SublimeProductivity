from __future__ import absolute_import, print_function
import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tweepy
import threading

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

class TwitterApiCall(threading.Thread):
	def __init__(self, timeout, instance, edit):
		self.timeout = timeout
		self.result = None
		self.instance = instance
		self.edit = edit
		threading.Thread.__init__(self)

	def run(self):
		try:
			auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			api = tweepy.API(auth)
			self.result = api.home_timeline()
			self.instance.print_tweets(self.result)

		except:
			self.result = False