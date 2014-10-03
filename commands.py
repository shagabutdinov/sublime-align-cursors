import sublime
import sublime_plugin

class AlignCursors(sublime_plugin.TextCommand):
  def run(self, edit):
    max_point = 0
    for cursor in self.view.sel():
      _, point = self.view.rowcol(cursor.b)
      if max_point < point:
        max_point = point

    for cursor in reversed(self.view.sel()):
      _, point = self.view.rowcol(cursor.b)
      if point < max_point:
        self.view.insert(edit, cursor.b, ' ' * (max_point - point))
