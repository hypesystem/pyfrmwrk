def error_html(message = ''):
    html = '<h1>Module Fault: Error in module code</h1><p>A module is not working correctly as it has been badly implemented. This is usually due to missing functions that are required by the framework.</p>'
    if len(message) > 0:
        html += '<p>The following message as given: %s</p>' % message
    return html
