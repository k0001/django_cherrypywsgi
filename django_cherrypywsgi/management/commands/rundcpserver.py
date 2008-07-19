from django.core.management.base import NoArgsCommand
from django.core.handlers.wsgi import WSGIHandler
from django.conf import settings
from django_cherrypywsgi import DjangoCherryPyWSGIServer
import os

class Command(NoArgsCommand):
    help = "Serve this django project as WSGI through CherryPy's WSGI server"

    requires_model_validation = False
    can_import_settings = True

    def handle_noargs(self, **options):
        os.environ['DJANGO_SETTINGS_MODULE'] = settings.ROOT_URLCONF
        wsgi_app = WSGIHandler()
        server = DjangoCherryPyWSGIServer(wsgi_app)
        try:
            server.start()
        except KeyboardInterrupt:
            server.stop()
