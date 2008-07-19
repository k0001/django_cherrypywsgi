from django_cherrypywsgi.lib import wsgiserver
from django.conf import settings

class DjangoCherryPyWSGIServer(wsgiserver.CherryPyWSGIServer):
    def __init__(self, wsgi_app):
        socket_file = getattr(settings,
            'DCPWSGI_BIND_SOCKET_FILE', None)
        if socket_file:
            bind = socket_file
        else:
            host = getattr(settings,
                'DCPWSGI_BIND_HOST', 'localhost')
            port = getattr(settings,
                'DCPWSGI_BIND_PORT', 8000)
            bind = (host, port)

        numthreads = getattr(settings,
            'DCPWSGI_NUM_THREADS', 10)
        server_name = getattr(settings,
            'DCPWSGI_SERVER_NAME', None)
        max_request = getattr(settings,
            'DCPWSGI_MAX_REQUESTS', -1)
        request_queue_size = getattr(settings,
            'DCPWSGI_REQUEST_QUEUE_SIZE', 5)
        timeout = getattr(settings,
            'DCPWSGI_CONNECTION_TIMEOUT', 10)
        shutdown_timeout = getattr(settings,
            'DCPWSGI_SHUTDOWN_TIMEOUT', 5)

        super(DjangoCherryPyWSGIServer, self).__init__(
                bind_addr=(host, port),
                wsgi_app=wsgi_app,
                numthreads=numthreads,
                server_name=server_name,
                max=max_request,
                request_queue_size=request_queue_size,
                timeout=timeout,
                shutdown_timeout=shutdown_timeout)

        self.protocol = getattr(settings,
            'DCPWSGI_PROTOCOL', 'HTTP/1.1')
        self.nodelay = getattr(settings,
            'DCPWSGI_NODELAY', True)
        self.ssl_certificate = getattr(settings,
            'DCPWSGI_SSL_CERTIFICATE', None)
        self.ssl_private_key = getattr(settings,
            'DCPWSGI_SSL_PRIVATE_KEY', None)

