from __future__ import absolute_import, print_function
import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sublime, sublime_plugin
import tweepy

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

class ProductivityCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		ProductivityCommand.open_new_file(self, edit)
		ProductivityCommand.print_tweets(self, edit)

	def open_new_file(self, edit):
		current_window = self.view.window()
		new_file = current_window.new_file()
		current_window.focus_view(new_file)
		active_view = current_window.active_view()
		active_view.set_name('TW.py')
		active_view.set_syntax_file('Packages/Python/Python.sublime-syntax')

	def print_tweets(self, edit):
		current_window = self.view.window()
		active_view = current_window.active_view()
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		active_view.insert(edit, 0, 'class Twitter(): \n')
		api = tweepy.API(auth)
		public_tweets = api.home_timeline()
		for tweet in public_tweets:
			active_view.insert(edit, active_view.size(), '    #time: ' + str(tweet.created_at) + '\n    #retweeted: ' + str(tweet.retweet_count) + '\n    #favorites: ' + str(tweet.favorite_count) + '    \n    def ' + tweet.user.name.lower().replace(' ', '_') + '(handle = "@' + tweet.user.screen_name + '"): \n        text = "' + tweet.text + '"\n\n')