# Open DOI

This is a package for [Sublime Text](https://www.sublimetext.com/). It opens digital object identifiers (DOIs) as URLs in your browser.

## Usage

If a DOI looks like `https://doi.org/10.1103/PhysRevLett.116.061102`, Sublime Text allows you to open it in a browser directly as an URL. In this case, you do not need to use this package.

But if a DOI looks like `10.1103/PhysRevLett.116.061102`, this package should help you. Select such a DOI and click `Open DOI` from the context menu. Then the selected DOI will be opened in your browser.

Multiple selection is supported: if you select multiple DOIs, they will be opened as separate URLs.

The leading and trailing whitespace characters are ignored.

If your selection does not match the DOI [syntax](https://www.doi.org/doi_handbook/2_Numbering.html#2.2) (i.e., it does not start with `10.` and does not contain `/`), it will be ignored.

## Installation

If/when this package is added to the Package Control [list](https://packagecontrol.io/browse), it is recommended to install it using [Package Control](https://packagecontrol.io/): press `Ctrl+Shift+P` (Win, Linux) or `Cmd+Shift+P` (Mac) and type `Package Control: Install Package` in the Command Palette. Then select `open doi` from the list.

Alternatively, download files `Context.sublime-menu`, `LICENSE`, `open_doi.py`, and `README.md` manually, put them into a ZIP archive, and rename this archive to `open_doi.sublime-package`. After that, run Sublime Text and click `Preferences / Browse Packages...`. File Explorer should be opened after that. In there, navigate one directory up, open `Installed Packages` directory, and put `open_doi.sublime-package` file into it.

## Changelog

* Version 1.0.0 (17 March 2021): initial release

----------

**Open DOI**

Version 1.0.0 (17 March 2021)

Copyright (c) 2021 Evgenii Shirokov

MIT License
