# -*- coding: utf-8 -*-

from game.models import Game
from db_file_storage.form_widgets import DBClearableFileInput
from django import forms


class FormGame(forms.ModelForm):
    class Meta:
        model = Game
        widgets = {
            'picture': DBClearableFileInput
        }