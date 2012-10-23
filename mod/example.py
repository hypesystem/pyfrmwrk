""" This is an example module, displaying some text from a html snippet... """

def body():
    return open('pfwhtml/snippet.example.htm').read()

def title():
    return "Example"
