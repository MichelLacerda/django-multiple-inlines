# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.views.generic.edit import CreateView
from django.forms.models import inlineformset_factory
from nested_formset import nestedformset_factory

from .models import (
    Client,
    Address,
    Attachment
)

from .forms import (
    ClientForm,
)


class CreateClient(CreateView):

    model = Client
    form_class = ClientForm

    def get_context_data(self, *args, **kwargs):
        ctx = super(CreateClient, self).get_context_data(*args, **kwargs)
        ctx['formset'] = nestedformset_factory(
            Client,
            Address,
            extra=1,
            nested_formset=inlineformset_factory(
                Address,
                Attachment,
                extra=1,
                fields='__all__'
            )
        )
        return ctx

create_contact = CreateClient.as_view()
