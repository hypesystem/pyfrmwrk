import hypehtmldesign

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
			  stylesheets: a tuple of CSS stylesheets to be included
			  scripts: a tuple of JavaScript scripts to be included
	    """
		# Verify types, then set values
        if type(body) is not string:
		    raise ValueError("The body argument must be a string")
		self.body = body
		if type(title) is not string:
		    raise ValueError("The title argument must be a string")
        self.title = title
		if type(charset) is not string:
		    raise ValueError("The charset argument must be a string")
        self.charset = charset
        if type(stylesheets) is not tuple and stylesheets is not None:
		    raise ValueError("The stylesheets argument must be a tuple or have no value")
        self.stylesheets = stylesheets
		if type(scripts) is not tuple and scripts is not None:
		    raise ValueError("The scripts argument must be a tuple or have no value")
        self.scripts = scripts
		if type(head) is not string:
		    raise ValueError("The head argument must be a string")
        self.head = head
		if type(design) is not HtmlDesign and design is not None:
		    raise ValueError("The design argument must be a hypehtml.HtmlDesign or have no value; Note: This may have been set wrongly through default design")
	    elif design is not None:
		    self.title = self.title + design.title_constant
			self.stylesheets = self.stylesheets + design.stylesheets
			self.scrips = self.scripts + design.scripts
        self.design = design
    def generate(self):
        """ Generates and returns the HTML for this page. """
		#body
		clean_body = self.clean_html(self.body)
		if design is not None:
			clean_design_body = self.clean_html(self.design.static_html)
			clean_body = design_body_html.replace("<%PFW_BODY%>",clean_body,1)
		#stylesheets
        stylesheets_html = ''
        if(self.stylesheets != None):
            for stl in self.stylesheets:
                stylesheets_html += '<link rel="stylesheet" type="text/css" href="%s">' % self.clean_resource_path(stl)
		#scripts
		scripts_html = ''
		if(self.scripts != None):
		    for sct in self.scripts:
			    scripts_html += '<script type="text/javascript" src="%s"></script>' % self.clean_resource_path(sct)
		#custom head
		clean_head = self.clean_html(self.head)
	    if design is not None:
		    clean_design_head = self.clean_html(self.design.static_html)
			clean_head = clean_design_head + clean_head
		#finalize
		head_html = '<title>%s</title><meta charset="%s">%s%s%s' % (self.title, self.charset, stylesheets_html, scripts_html, clean_head)
        full_html = "Content-Type: text/html;\n\n<!DOCTYPE html><html><head>%s</head><body>%s</body></html>" % (head_html, clean_body)
        return full_html
	#TODO: generate_as_stream(): For big pages, this lets you start sending data to the server while it is being generated, no need to save anything
	@staticmethod
	def clean_resource_path(resource_path):
	    """ Cleans the path of the resource, preferring minified versions if possible """
		# TODO:if relative path (not full)
		# TODO: Check if .min.<ext> version exists, prefer this
		# TODO: Check if path is correct, force /res=<file> if /res/<file> or <file>, otherwise raise exception
		return resource_path
	@staticmethod
	def clean_html(html):
	    """ Cleans the given HTML, making it as small as possible """
		result = ''
		html_lines = html.split('\n')
		for line in html_lines:
		    result += ' ' + line.strip()
		return result