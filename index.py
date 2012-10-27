#!/usr/bin/env python3
# This file enables CGI debugging, is the file run as CGI and then lets the controller do its job
# enable debugging
from datetime import datetime
startprocess = datetime.now().microsecond
import cgitb
cgitb.enable()

# Import and run controller
import controller

timespent = datetime.now().microsecond - startprocess
print("<!-- Time spent on page generation: %d ms -->" % (timespent / 1000))

