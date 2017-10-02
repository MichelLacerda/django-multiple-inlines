# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Client(models.Model):
    """Cliente."""

    first_name = models.CharField(
        _(u'Primeiro nome'),
        max_length=255,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        _(u'Segundo nome'),
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return u"{0} {1}".format(self.first_name, self.last_name)


@python_2_unicode_compatible
class Address(models.Model):
    """Contatos do Cliente."""

    street = models.CharField(
        _(u'Rua/Av'),
        max_length=255,
        blank=True,
        null=True
    )

    number = models.PositiveIntegerField(
        _(u'Nº'),
        blank=True,
        null=True
    )

    zip_code = models.CharField(
        _(u'CEP'),
        max_length=10,
        blank=True,
        null=True
    )

    client = models.ForeignKey(
        Client,
        related_name='address',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Attachment(models.Model):
    """Anexos do Contato."""

    attachment = models.FileField(
        upload_to='attachment/'
    )

    address = models.ForeignKey(
        Address,
        related_name='attachment',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.attachment.filename or 'No file'
