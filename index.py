#!/usr/bin/env python3
# This file enables CGI debugging, is the file run as CGI and then lets the controller do its job
# enable debugging
import cgitb
cgitb.enable()

# Import and run controller
import controller
