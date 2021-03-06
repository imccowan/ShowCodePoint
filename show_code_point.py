import sublime_plugin

from unicodedata import name


class ShowCodePoint(sublime_plugin.TextCommand):

    def run(self, edit):
        if len(self.view.sel()) == 1:
            # Getting caret position.
            (row, col) = self.view.rowcol(self.view.sel()[0].begin())
            char = self.view.substr(self.view.text_point(row, col))

            statusKey = self.view.settings().get("codepoint_status_key",
                                                 "codepoint")
            if self.view.get_status(statusKey):
                self.view.erase_status(statusKey)
            else:
                statusStr = "{0} [<{1}> {2:d}, Hex {2:x}, Octal {2:o}]".format(
                    name(char), char, ord(char)
                )
                self.view.set_status(statusKey, statusStr)


class ResetCodePointStatus(sublime_plugin.EventListener):

    def on_selection_modified(self, view):
        statusKey = view.settings().get("codepoint_status_key",
                                        "codepoint")
        view.erase_status(statusKey)
