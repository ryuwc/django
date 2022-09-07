from cProfile import label
from dataclasses import field
from django import forms
from .models import Movies

class MoviesForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '세 얼간이'
            }
        )
    )

    director = forms.CharField(
        label='감독',
        widget=forms.TextInput(
            attrs={
                'placeholder': '라지쿠마르 히라니'
            }
            
        )
    )

    comment = forms.CharField(
        label='댓글',
        widget=forms.Textarea(
            attrs={
                'placeholder': '나 얼간이 아니다!',
                'rows':3,
                'cols':40,
            }
        )
    )

    class Meta:
        model = Movies
        fields = '__all__'