from django import forms
from .models import Ad


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'descpition', 'image']
        labels = {
            'title': 'Название объявления',
            'descpition': 'Описание объявления',
            'image': 'Выберите файл'
        }

        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Название объявления'
            }),
            'descpition': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание объявления'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'type': 'file'
            })
        }