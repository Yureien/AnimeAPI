from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'


class ApiConfig(AppConfig):
    name = 'api'
