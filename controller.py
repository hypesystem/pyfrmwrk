import hypehtml
import settings
import sys
import cgi
import error

def die(message = ''):
    """ Kills the page from further process with one final message printed """
    print(message)
    sys.exit()

# Standard design
design = hypehtml.HtmlDesign(title_constant = settings.design.title_constant, static_html = settings.design.htmlwrap, stylesheets = settings.design.stylesheets, scripts = settings.design.scripts)
hypehtml.HtmlPage.set_default_design(design)

# Get module from GET, if not set, set as default:
modulename = settings.general.default_module
args = cgi.FieldStorage()
if len(args) > 0:
    if "show" in args:
        modulename = args["show"].value

try:
    modulepath = "mod.%s" % modulename
    module = __import__(modulepath, fromlist=["mod"])
except ImportError:
    page = hypehtml.HtmlPage(error.e404.error_html())
    die(page.generate())

page_arguments = dict()
# Try to get all page information from module
# Body [REQUIRED!]
try:
    body = module.body
    page_arguments.update(dict(body = body))
except AttributeError:
    page = hypehtml.HtmlPage(error.eModuleFault.error_html("Module has no body() function, which should return the html body of the page to be displayed"))
    die(page.generate())
# Title
try:
    title = module.title
    page_arguments.update(dict(title = title))
except AttributeError:
    1
    # Ignore this
# Charset
try:
    charset = module.charset
    page_arguments.update(dict(charset = charset))
except AttributeError:
    1
    # Ignore this
try:
    stylesheets = module.stylesheets
    page_arguments.update(dict(stylesheets = stylesheets))
except AttributeError:
    1
    # Ignore this
try:
    scripts = module.scripts
    page_arguments.update(dict(scripts = scripts))
except AttributeError:
    1
    # Ignore this
try:
    head = module.head
    page_arguments.update(dict(head = head))
except AttributeError:
    1
    # Ignore this
try:
    design = module.design
    page_arguments.update(dict(design = design))
except AttributeError:
    1
    # Ignore this

page = hypehtml.HtmlPage(**page_arguments)

print(page.generate())
