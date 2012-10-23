PyFrmWrk - Simple Python Web with CGI
=====================================

* Generate correct HTML5 pages
* Minimize file sizes to transfer as little as possible
* Easily extensible through modules

Control
-------

The `.htaccess` file sets index.py as an index and does the necessary rewrite.
The purpose of the index is enabling debugging and passing on handling to the
controller (a bit redundant, might be cleaned). The controller handles checking
GET arguments, looking to see if modules exist, etc.

hypehtml
--------

The hypehtml module generates valid HTML5 pages. It also takes designs that are
general setups of pages.