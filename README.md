# Open DOI

This package provides a new command in the context menu and the Command Palette of [Sublime Text](https://www.sublimetext.com/) to open the selected digital object identifiers (DOIs), that are formatted without `https://doi.org/` and look like `10.1103/PhysRevLett.116.061102`, as URLs in your browser.

## Usage

If a DOI looks like `https://doi.org/10.1103/PhysRevLett.116.061102`, Sublime Text allows you to open it in a browser directly as an URL. In this case, you do not need to use this package.

But if a DOI looks like `10.1103/PhysRevLett.116.061102`, this package should help you. Select such a DOI and click on `Open DOI` in the context menu or in the Command Palette. Then the selected DOI will be opened in your browser.

Multiple selection is supported: if you select multiple DOIs, they will be opened as separate URLs.

The leading and trailing whitespace characters in your selection are ignored.

If your selection does not match the basic DOI [syntax](https://www.doi.org/doi_handbook/2_Numbering.html#2.2) (i.e., it does not start with `10.` and does not contain `/`), it will be ignored.

## Installation

It is recommended to install it using [Package Control](https://packagecontrol.io/): press `Ctrl+Shift+P` (Win, Linux) or `Cmd+Shift+P` (Mac) and type `Package Control: Install Package` in the Command Palette. Then select `Open DOI` from the list.

Alternatively, download files `Context.sublime-menu`, `Default.sublime-commands`, `LICENSE`, `open_doi.py`, and `README.md` manually, put them into a ZIP archive, and rename this archive to `Open DOI.sublime-package`. After that, run Sublime Text and click on `Preferences / Browse Packages...`. File Explorer should be opened after that. In there, navigate one directory up, open `Installed Packages` directory, and put `Open DOI.sublime-package` file into it.

## Changelog

* Version 1.0.0 (17 March 2021): initial release

----------

**Open DOI**

Version 1.0.0 (17 March 2021)

Copyright (c) 2021 Evgenii Shirokov

MIT License
