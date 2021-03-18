''' Open DOI
    Version 1.0.0 (17 March 2021)
    Copyright (c) 2021 Evgenii Shirokov
    MIT License
'''

import sublime
import sublime_plugin
import webbrowser


class OpenDoiCommand(sublime_plugin.TextCommand):
    '''Open the DOI, selected in Sublime Text, as an URL in your browser.'''
    def run(self, edit):
        opened = False
        for region in self.view.sel():
            doi = self.view.substr(region).strip()
            if doi.startswith('10.') and ('/' in doi):
                webbrowser.open('https://doi.org/' + doi)
                opened = True
        if not opened:
            sublime.status_message('Wrong DOI syntax!')
