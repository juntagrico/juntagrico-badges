from django.apps import AppConfig


class JuntagricoAppconfig(AppConfig):
    name = "juntagrico_badges"
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from juntagrico.util import addons
        addons.config.register_version(self.name)
