''' Open DOI
    Version 1.0.3 (2021-07-30)
    Copyright (c) 2021 Evgenii Shirokov
    MIT License
'''

import sublime
import sublime_plugin
import webbrowser


class OpenDoiCommand(sublime_plugin.TextCommand):
    '''Open the DOI/shortDOI, selected in Sublime Text, in your browser.'''

    doi_list = []

    def run(self, edit):
        for doi in OpenDoiCommand.doi_list:
            webbrowser.open('https://doi.org/' + doi)

    def is_visible(self):
        OpenDoiCommand.doi_list.clear()
        for selection in self.view.sel():
            string = self.view.substr(selection).strip()
            if (string.startswith('10.') and ('/' in string)) \
               or string.startswith('10/'):
                OpenDoiCommand.doi_list.append(string)
        return OpenDoiCommand.doi_list != []
