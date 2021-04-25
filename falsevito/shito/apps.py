from django.apps import AppConfig


class ShitoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shito'


    def ready(self):
        from . import signals
