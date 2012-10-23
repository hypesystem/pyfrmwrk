import cgi

getargs = cgi.FieldStorage()

def body():
    result = '%d<br>' % len(getargs)
    for key in getargs.keys():
        result += "%s => %s<br>" % (key, getargs[key].value)
    return result

def title():
    return "ArgPrinter"
