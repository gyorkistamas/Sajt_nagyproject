from click import option
from django.contrib.auth.management.commands import createsuperuser
from django.core.management.base import CommandError


class Command(createsuperuser.Command):
    def handle(self, *args, **options):
        try:
            options['is_staff'] = True
            options['is_superuser'] = True
            super().handle(*args, **options)
        except CommandError as e:
            if 'superuser' not in e.args[0]:
                raise