import urlparse

def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    parameters = urlparse.parse_qsl(environ.get("QUERY_STRING"))
    body = ["{}={}".format(par, val) for (par, val) in parameters]
    body = "\r\n".join(body)
    start_response(status, headers)
    return [body]
    