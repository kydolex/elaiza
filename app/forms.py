from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())

class BlogCommentForm(forms.Form):
    content = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'cols': '30', 'rows': '7'}))
