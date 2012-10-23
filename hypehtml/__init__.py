default_design = None

def setDefaultDesign(design):
    default_design = design


# A valid HTML5 page
#  title: The title tag in head, the title displayed on the browser window
#  charset: The charset of the website. Defaults to 'utf8'
#  stylesheets: An array of stylesheets to be used
#  scripts: An array of scripts to be used
#  head: HTML to be included inside the head tag
#  body: HTML to be included inside the body tag
# TODO: Move this to be doc comment of constructor!
class HtmlPage:
    def __init__(self, body, title = '', charset = 'utf8', stylesheets = None, scripts = None, head = '', design = default_design):
        self.body = body
        self.title = title
        self.charset = charset
# TODO: Verify these as arrays
        self.stylesheets = stylesheets
        self.scripts = scripts
        self.head = head
# TODO: Verify is actually design
        self.design = design
    def generate(self):
        """ Generates and returns the HTML for this page. """
        stylesheets_html = ''
        if(self.stylesheets != None):
            for stl in self.stylesheets:
                stylesheets_html += '<link rel="stylesheet" type="text/css" href="%s">' % stl
        
        result = "Content-Type: text/html;\n\n<!DOCTYPE html><html><head><title>%s</title><meta charset=\"%s\">%s%s</head><body>%s</body></html>" % (self.title, self.charset, stylesheets_html, self.head, self.body)
        return result

# TODO: UNFINISHED! Maybe delete?
class HtmlDesign:
    """ A general design that may be applied to several HtmlPages, resulting in a general style """
    def __init__(self, statichtml = '%%CONTENT%%', stylesheets = None, scripts = None, head = ''):
        """ Creates a new design. When statichtml is provided, it must contain %%CONTENT%%, in which the
            content body of the page is held
        """
        self.statichtml = statichtml
        self.stylesheets = stylesheets
        self.scripts = scripts
        self.head = head
    def statichtml():
        return statichtml
    def stylesheets():
        return stylesheets
    
