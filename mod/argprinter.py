import cgi

getargs = cgi.FieldStorage()

def body_make():
    result = '%d<br>' % len(getargs)
    for key in getargs.keys():
        result += "%s => %s<br>" % (key, getargs[key].value)
    return result

def title_make():
    return "ArgPrinter"

body = body_make()
title = title_make()
