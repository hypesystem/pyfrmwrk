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