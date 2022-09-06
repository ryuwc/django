import imp
from socket import fromshare
from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summury = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'summury',
                'maxlength': 20,
            }
        )
    )

    memo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'memo',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Memo
        fields = '__all__'
