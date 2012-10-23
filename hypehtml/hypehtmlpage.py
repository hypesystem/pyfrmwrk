default_design = None

def set_default_design(design):
    """ Set the default design of any HTML page """
    default_design = design

class HtmlPage:
    """ A valid HTML5 page with Content-Type header """
    def __init__(self, body, title = '', charset = 'utf8', stylesheets = None, scripts = None, head = '', design = default_design):
	    """ Creates a HtmlPage, taking the following arguments:
		      body (required): HTML to be included inside the body tag
			  head: HTML to be included inside the head tag
			  title: content of title tag in head, title displayed in browser window
			  charset: string representation of charset of page, used in the charset meta-tag
			  stylesheets: an array of CSS stylesheets to be included
			  scripts: an array of JavaScript scripts to be included
	    """
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