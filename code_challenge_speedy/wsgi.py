import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_challenge_speedy.settings')
application = get_wsgi_application()
