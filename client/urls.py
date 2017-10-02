# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url

from .views import (
    create_contact,
)


urlpatterns = [
    url(r'^create/$', create_contact, name='create'),
]
