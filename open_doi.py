''' Open DOI
    Version 1.0.1 (2021-03-20)
    Copyright (c) 2021 Evgenii Shirokov
    MIT License
'''

import sublime
import sublime_plugin
import webbrowser


class OpenDoiCommand(sublime_plugin.TextCommand):
    '''Open the DOI, selected in Sublime Text, as an URL in your browser.'''

    doi_list = []

    def run(self, edit):
        for doi in OpenDoiCommand.doi_list:
            webbrowser.open('https://doi.org/' + doi)

    def is_visible(self):
        OpenDoiCommand.doi_list.clear()
        for selection in self.view.sel():
            string = self.view.substr(selection).strip()
            if string.startswith('10.') and ('/' in string):
                OpenDoiCommand.doi_list.append(string)
        return OpenDoiCommand.doi_list != []
