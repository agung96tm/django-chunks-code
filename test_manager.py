#!/usr/bin/env python

import sys
import django
from django.conf import settings
from django.test.utils import get_runner


if __name__ == '__main__':
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        # ROOT_URLCONF='tests.urls',
        INSTALLED_APPS=[
            'src.common',
            'src.rest',
        ]
    )
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
