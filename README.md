# Open DOI

This package provides a new command in the context menu and the Command Palette of [Sublime Text](https://www.sublimetext.com/) to open the selected digital object identifiers (DOIs) or shortDOIs, that are formatted without `https://doi.org/` and look like `10.1103/PhysRevLett.116.061102` or `10/gcp5km`, as URLs in your browser. 

## Usage

If a DOI looks like `https://doi.org/10.1103/PhysRevLett.116.061102`, Sublime Text allows you to open it in a browser directly as an URL. In this case, you do not need to use this package.

But if a DOI looks like `10.1103/PhysRevLett.116.061102`, this package should help you. Select such a DOI and click on `Open DOI` in the context menu or in the Command Palette. Then the selected DOI will be opened in your browser. Moreover, shortDOIs (e.g., `10/gcp5km`) are supported.

Multiple selection is supported: if you select multiple DOIs/shortDOIs, they will be opened as separate URLs.

The leading and trailing whitespace characters in your selection are ignored.

If your selection does not match the basic DOI [syntax](https://www.doi.org/doi_handbook/2_Numbering.html#2.2) (i.e., it does not start with `10.` and does not contain `/`) or shortDOI [syntax](https://shortdoi.org/) (i.e., it does not start with `10/`), it will be ignored.

## Installation

It is recommended to install this package using [Package Control](https://packagecontrol.io/): type `Package Control: Install Package` in the Command Palette and select `Open DOI` from the list.

It is possible to install this package manually as well.

## Changelog

* Version 1.0.3 (2021-07-30): add shortDOI support

* Version 1.0.2 (2021-03-20): correct README.md

* Version 1.0.1 (2021-03-20): add is_visible() check

* Version 1.0.0 (2021-03-17): initial release

----------

**Open DOI**

Version 1.0.3 (2021-07-30)

Copyright (c) 2021 Evgenii Shirokov

MIT License
