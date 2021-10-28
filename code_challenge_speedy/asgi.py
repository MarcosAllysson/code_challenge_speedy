import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_challenge_speedy.settings')
application = get_asgi_application()
