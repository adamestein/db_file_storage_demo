# -*- coding: utf-8 -*-

from console.models import Console
from db_file_storage.form_widgets import DBClearableFileInput
from django import forms


class FormConsole(forms.ModelForm):
    class Meta:
        model = Console
        widgets = {
            'picture': DBClearableFileInput
        }