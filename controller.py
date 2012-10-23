import hypehtml
import settings
import sys
import cgi
import error

def die(message = ''):
    """ Kills the page from further process with one final message printed """
    print message
    sys.exit()

# TODO: Get module from GET, if not set, set as default:
modulename = settings.general.default_module
args = cgi.FieldStorage()
if(len(args) > 0):
    if("show" in args):
        modulename = args["show"].value

try:
    # TODO: This import statement somehow prints "Content-Type: text/html,
    #       supposedly by running index.py
    modulepath = "mod.%s" % modulename
    module = __import__(modulepath, fromlist=["mod"])
except ImportError:
    page = hypehtml.HtmlPage(error.e404.error_html())
    die(page.generate())

# Try to get all page information from module
try:
    body = module.body()
except AttributeError:
    page = hypehtml.HtmlPage(error.eModuleFault.error_html("Module has no body() function, which should return the html body of the page to be displayed"))
    die(page.generate())

page = hypehtml.HtmlPage(body, title=module.title()+settings.design.title_constant,stylesheets=settings.design.stylesheets)

print page.generate()
