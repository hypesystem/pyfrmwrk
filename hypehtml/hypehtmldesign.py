class HtmlDesign:
    """ A general design that may be applied to several HtmlPages, resulting in a general style """
    def __init__(self, static_html = '<%PFW_BODY%>', stylesheets = None, scripts = None, head = '', title_constant = ''):
        """ Creates a new design. When statichtml is provided, it must contain %%CONTENT%%, in which the
            content body of the page is held
        """
        self.static_html = static_html
        self.stylesheets = stylesheets
        self.scripts = scripts
        self.head = head
		self.title_constant = title_constant
    def statichtml():
        return statichtml
    def stylesheets():
        return stylesheets