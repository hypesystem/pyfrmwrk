""" This module is a simple home page, including a snippet file and returning it to the controller to print """

title = "Home"
body = open('pfwhtml/snippet.home.htm','r').read()
