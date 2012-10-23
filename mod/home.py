""" This module is a simple home page, including a snippet file and returning it to the controller to print """

snippetfile = open('pfwhtml/snippet.home.htm','r')
snippetcontent = snippetfile.read()

def title():
    return "PyFrmWrk/Home"
def body():
    return snippetcontent
