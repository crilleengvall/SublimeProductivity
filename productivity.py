import sublime, sublime_plugin
from twitterapicall import TwitterApiCall

class ProductivityCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		ProductivityCommand.open_new_file(self, edit)
		ProductivityCommand.print_loading_message(self, edit)
		ProductivityCommand.call_twitter_api(self, edit)

	def open_new_file(self, edit):
		current_window = self.view.window()
		new_file = current_window.new_file()
		current_window.focus_view(new_file)
		active_view = current_window.active_view()
		active_view.set_name('TW.py')
		active_view.set_syntax_file('Packages/Python/Python.sublime-syntax')

	def print_loading_message(self, edit):
		current_window = self.view.window()
		active_view = current_window.active_view()
		active_view.insert(edit, 0, 'Loading tweets...\n')

	def call_twitter_api(self, edit):
		thread = TwitterApiCall(5, self, edit)
		thread.start()

	def print_tweets(self, result):
		add_class = True
		for tweet in result:
			self.view.run_command('tweet_printer', {"created_at" : str(tweet.created_at), 
				"add_class" : add_class, "retweet_count" : str(tweet.retweet_count),
				"favorite_count" : str(tweet.favorite_count),
				"user_name": tweet.user.name, "screen_name" : tweet.user.screen_name,
				"text" : tweet.text })
			add_class = False

class TweetPrinterCommand(sublime_plugin.TextCommand):
	def run(self, edit, created_at, add_class, retweet_count, favorite_count, user_name, screen_name, text):
		current_window = self.view.window()
		active_view = current_window.active_view()
		if add_class == True:
			active_view.insert(edit, active_view.size(), 'class Twitter(): \n')
		
		active_view.insert(edit, active_view.size(), '    #time: ' + created_at + '\n    #retweeted: ' + retweet_count + '\n    #favorites: ' + favorite_count + '    \n    def ' + user_name.lower().replace(' ', '_') + '(handle = "@' + screen_name + '"): \n        text = "' + text + '"\n\n')
		