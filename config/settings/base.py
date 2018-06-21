# settings/base.py
import os
import json

# Normally you should not import ANYTHING from django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


# JSON-based secrets module
current_file_dir = os.path.dirname(__file__)
file_path = os.path.join(current_file_dir, 'secrets.json')
with open(file_path) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.'''
    try:
    	return secrets[setting]
    except KeyError:
    	error_msg = 'Set the {0} environment variable'.format(setting)
    	raise ImproperlyConfigured(error_msg)
