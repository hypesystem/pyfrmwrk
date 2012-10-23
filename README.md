PyFrmWrk - Simple Python Web with CGI
=====================================

* Generate correct HTML5 pages
* Minimize file sizes to transfer as little as possible
* Easily extensible through modules

Control
-------

The `.htaccess` file sets `index.py` as an index and does the necessary rewrite.
The purpose of the index is enabling debugging and passing on handling to the
controller (a bit redundant, might be cleaned). The controller handles checking
GET arguments, looking to see if modules exist, etc.

Structure
---------

### error

Contains content for common error pages.

### hypehtml

The hypehtml module generates valid HTML5 pages. It also takes designs that are
general setups of pages.

### mod

Contains modules. No HTML should be held here, but should instead go in `pfwhtml`.
This provides separation between model and view, only the model of the modules
should be held in the `mod` package.

The `__init__.py` file in the package automatically imports all modules.

### pfwhtml

Contains HTML snippets with PFW Variables (To Be Defined).

### pfwutil

Contains common PyFrmWrk utilities.

### settings

Contains all kinds of settings for the framework.