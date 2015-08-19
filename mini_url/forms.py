__author__ = 'PHUONG'

from django import forms
from .models import MiniURL
from tinymce.widgets import TinyMCE

class MiniURLForm(forms.ModelForm):
    ghi_chu = forms.CharField(widget=TinyMCE(attrs={'cols': 20, 'rows': 10}))
    class Meta:
        model = MiniURL
        fields = ('url', 'pseudo', 'ghi_chu')

    class Media:
        js = ()

