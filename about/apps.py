from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configures the 'about' application.

    Attributes:
        default_auto_field (str): Default primary key type ('BigAutoField').
        name (str): Application name ('about').
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
