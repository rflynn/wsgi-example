from cgi import parse_qs, escape

def hello_world(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    subject = escape(parameters['subject'][0] if 'subject' in parameters else 'World')
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['Hello %s' % subject]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 3031, hello_world)
    srv.serve_forever()
