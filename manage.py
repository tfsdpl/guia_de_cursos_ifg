#!/usr/bin/env python
import os
import sys


def importador_rreo():
    from importador import importaor_rreo
    importaor_rreo()


if __name__ == "__main__":
    if sys.argv[1] == 'rreo':
        print('ok')
        importador_rreo()

    settings = 'djangocore.tests.test_settings' if 'test' in sys.argv else 'djangocore.configs'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
