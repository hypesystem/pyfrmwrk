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

### res

Resources folder for front-end accessible resources (stylesheets and scripts).

### settings

Contains all kinds of settings for the framework.

Designing Modules
-----------------

Designing a module should be pretty straight forward. The first step is creating a
python file in the `mod/` directory. This is your module, representing the model of
the page in question. Once the module has been created it can be found at
`<HOST_NAME>/<MODULE_NAME>` - nice and clean URL.

The contents of the module is entirely made up of python code. There is nothing
special or fancy here. All you must do to make it work with the framework (if you've
run it before doing this, you'll have noticed an error) is to include some of the
following variables to be publicly accessible in your module:

    body *      HTML that will be put in the body-tag
    head        HTML that will be put in the head-tag
    charset     Charset of the page, set in meta-tag, defaults to "utf8"
    stylesheets Tuple of stylesheet URLs to be included, both relative and
                full paths are allowed.
    scripts     Tuple of script URLs to be included, both relative and full
                paths are allowed.
    design      A hypehtml.hypehtmldesign.HtmlDesign that will dictate general
                features of the page. The benefit of designs is that they can
                be reused.

Entries marked with * are required. Stylesheets and scripts should be placed in the
`res` folder and should be referred to as `/res/<filename>`.

Planned features
----------------

* HTML parser with syntax for including variables defined in code
* Deployment feature compiling all python code and minifying resources
