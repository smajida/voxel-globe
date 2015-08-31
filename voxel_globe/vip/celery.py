from __future__ import absolute_import

import os
from os import environ as env

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', env['VIP_DJANGO_SETTINGS_MODULE'])
#Really set by common.bat...

import boxm2_register
boxm2_register.smart_register = True
#This need to me imported before other boxm2 because of how it's designed
#This should take care of all boxm2 calls in Django and celery alike

#app = Celery('voxel_globe') #???
#app = Celery(env['VIP_CELERY_APP']);
app = Celery('voxel_globe.vip');

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))