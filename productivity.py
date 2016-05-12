import sublime, sublime_plugin

class ProductivityCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		ProductivityCommand.open_new_file(self, edit)


	def open_new_file(self, edit):
		current_window = self.view.window()
		new_file = current_window.new_file()
		current_window.focus_view(new_file)
		active_view = current_window.active_view()
		active_view.set_name('TW.py')