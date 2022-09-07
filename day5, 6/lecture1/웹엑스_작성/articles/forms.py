from django import forms

class ArticleForm(forms.Form):
    # 폼필드는 디폴트 위젯을 가진다.
    # 위젯은 렌더링 될때 html 태그로 변환된다.
    title = forms.CharField(max_length=10)
    content = forms.CharField(
        widget=forms.Textarea
    )