# -*- coding: utf-8 -*-

from django import forms
from django.forms import inlineformset_factory

from .models import (
    Client,
    Address,
    Attachment
)


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        field = (
            'first_name',
            'last_name',
        )
        exclude = ()
        widgets = {}


class ClientAddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = ()


class AddressAttachmentForm(forms.ModelForm):

    class Meta:
        model = Attachment
        exclude = ()


# Inlines

"""
inlineformset_factory(
    parent_model,
    model,
    form=ModelForm,
    formset=BaseInlineFormSet,
    fk_name=None,
    fields=None,
    exclude=None,
    extra=3,
    can_order=False,
    can_delete=True,
    max_num=None,
    formfield_callback=None,
    widgets=None,
    validate_max=False,
    localized_fields=None,
    labels=None,
    help_texts=None,
    error_messages=None,
    min_num=None,
    validate_min=False,
    field_classes=None
)
"""

ClientAddressInline = inlineformset_factory(
    Client,
    Address,
    form=ClientAddressForm,
    extra=1,
    max_num=3
)


AddressAttachmentInline = inlineformset_factory(
    Address,
    Attachment,
    form=AddressAttachmentForm,
    extra=1,
    max_num=3
)
