import imp
from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     NARION_A = 'kr'
#     NARION_B = 'jp'
#     NARION_C = 'ch'
#     NATIONS_CHOICES = [
#         (NARION_A, '한국'),
#         (NARION_B, '일본'),
#         (NARION_C, '중국'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
    # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-class form-control',
                'placeholder': 'Enter the content',
                'row': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': "내용 입력해"
        }
    )


    class Meta:
        # 어떤 모델을 기반으로 할지
        model = Article
        # 어떤 모델필드 중 어떤 것을 출력할지
        fields = '__all__'
        # exclude = ('title')