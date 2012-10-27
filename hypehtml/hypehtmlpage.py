from .hypehtmldesign import HtmlDesign
import os

class HtmlPage:
    """ A valid HTML5 page with Content-Type header """
    default_design = None
    def __init__(self, body, title = '', charset = 'utf8', stylesheets = None, scripts = None, head = '', design = None):
        """ Creates a HtmlPage, taking the following arguments:
              body (required): HTML to be included inside the body tag
              head: HTML to be included inside the head tag
              title: content of title tag in head, title displayed in browser window
              charset: string representation of charset of page, used in the charset meta-tag
              stylesheets: a tuple of CSS stylesheets to be included
              scripts: a tuple of JavaScript scripts to be included
        """
        # Verify types, then set values
        if type(body) is not str:
            raise ValueError("The body argument must be a string (%s)" % body)
        self.body = body
        if type(title) is not str:
            raise ValueError("The title argument must be a string (%s)" % title)
        self.title = title
        if type(charset) is not str:
            raise ValueError("The charset argument must be a string (%s)" % charset)
        self.charset = charset
        if type(stylesheets) is not tuple and stylesheets is not None:
            raise ValueError("The stylesheets argument must be a tuple or have no value (%s)" % stylesheets)
        self.stylesheets = stylesheets
        if type(scripts) is not tuple and scripts is not None:
            raise ValueError("The scripts argument must be a tuple or have no value (%s)" % scripts)
        self.scripts = scripts
        if type(head) is not str:
            raise ValueError("The head argument must be a string (%s)" % head)
        self.head = head
        if design is None and HtmlPage.default_design is not None:
            design = HtmlPage.default_design
        if not isinstance(design,HtmlDesign) and design is not None:
            raise ValueError("The design argument must be a %s or have no value; Note: This may have been set wrongly through default design (is %s)" % (HtmlDesign, design))
        elif design is not None:
            self.title = self.title + design.title_constant
            if design.stylesheets is not None:
                if self.stylesheets is not None:
                    self.stylesheets = design.stylesheets + self.stylesheets
                else:
                    self.stylesheets = design.stylesheets
            if design.scripts is not None:
                if self.scripts is not None:
                    self.scripts = design.scripts + self.scripts
                else:
                    self.scripts = design.scripts
        self.design = design
    def generate(self):
        """ Generates and returns the HTML for this page. """
        #body
        clean_body = self.clean_html(self.body)
        if self.design is not None:
            clean_design_body = self.clean_html(self.design.static_html)
            clean_body = clean_design_body.replace("<%PFW_BODY%>",clean_body,1)
        #stylesheets
        stylesheets_html = ''
        if self.stylesheets is not None:
            for stl in self.stylesheets:
                stylesheets_html += '<link rel="stylesheet" type="text/css" href="%s">' % self.clean_resource_path(stl)
        #scripts
        scripts_html = ''
        if self.scripts is not None:
            for sct in self.scripts:
                scripts_html += '<script type="text/javascript" src="%s"></script>' % self.clean_resource_path(sct)
        #custom head
        clean_head = self.clean_html(self.head)
        if self.design is not None:
            clean_design_head = self.clean_html(self.design.head)
            clean_head = clean_design_head + clean_head
        #finalize
        head_html = '<title>%s</title><meta charset="%s">%s%s%s' % (self.title, self.charset, stylesheets_html, scripts_html, clean_head)
        full_html = "Content-Type: text/html;\n\n<!DOCTYPE html><html><head>%s</head><body>%s</body></html>" % (head_html, clean_body)
        return full_html
    #TODO: generate_as_stream(): For big pages, this lets you start sending data to the server while it is being generated, no need to save anything
    @staticmethod
    def clean_resource_path(resource_path):
        """ Cleans the path of the resource, preferring minified versions if possible """
        # Fit rewrite format (res=(.*))
        is_relative_path = False
        if resource_path[0:4] == "res/":
            resource_path = "/res=" + resource_path[4:]
            is_relative_path = True
        elif resource_path[0:5] == "/res/":
            resource_path = "/res=" + resource_path[5:]
            is_relative_path = True
        elif resource_path[0] == "/":
            resource_path = "/res=" + resource_path[1:]
            is_relative_path = True
        # Check if .min.<ext> version exists, prefer this
        if is_relative_path:
            resource_ext_isolated = resource_path.rpartition(".")
            minified_path = resource_ext_isolated[0] + ".min." + resource_ext_isolated[1]
            if(os.path.exists("./res/" + minified_path[5:])):
                resource_path = minified_path
        return resource_path
    @staticmethod
    def clean_html(html):
        """ Cleans the given HTML, making it as small as possible """
        result = ''
        html_lines = html.split('\n')
        for line in html_lines:
            result += ' ' + line.strip()
        return result
    @staticmethod
    def set_default_design(design):
        HtmlPage.default_design = design
