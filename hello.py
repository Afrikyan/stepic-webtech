import urlparse

def wsgi_hello(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    parameters = urlparse.parse_qsl(environ.get("QUERY_STRING"))
    body = ["{}={}".format(par, val) for (par, val) in parameters]
    body = "\n".join(body)
    return [body]
    