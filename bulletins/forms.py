from django import forms

from .models import Bulletin


class BulletinForm(forms.ModelForm):
    category__name = forms.CharField(max_length=80)
    title = forms.CharField(max_length=100)
    content = forms.TextInput()
    image = forms.FileField()

    class Meta:
        model = Bulletin
        fields = "__all__"
    
