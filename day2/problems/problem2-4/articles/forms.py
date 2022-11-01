from django import forms
from articles.models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('author',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]