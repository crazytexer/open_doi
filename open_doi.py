import sublime
import sublime_plugin
import webbrowser


class OpenDoiCommand(sublime_plugin.TextCommand):
    """Open the selected text as DOI link in your browser."""
    def run(self, edit):
        queries = []
        for region in self.view.sel():
            if not region.empty():
                queries.append(self.view.substr(region))
        for doi in queries:
            doi = doi.strip()
            if doi.startswith('10.') and ('/' in doi):
                webbrowser.open("https://doi.org/" + doi)
