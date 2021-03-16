from django import forms

from .models import Circle
class CircleForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class CircleModelForm(forms.ModelForm):
    practice_date = forms.CharField(label='活動日',widget=forms.TextInput(attrs={
        'placeholder': '例) 平日毎日、月～水 etc...'
    }))
    practice_place = forms.CharField(label='活動場所',widget=forms.TextInput(attrs={
        'placeholder': '例) 小机、多摩川 etc...'
    }))
    twitter_url = forms.URLField(widget=forms.TextInput(attrs={
        'placeholder': '例) https://twitter.com/keiotennis'
    }))
    insta_url = forms.URLField(widget=forms.TextInput(attrs={
        'placeholder': '例) https://www.instagram.com/keiotennis'
    }))
    line_url = forms.URLField(widget=forms.TextInput(attrs={
        'placeholder': '例) https://line.me/keiotennis'
    }))
    class Meta:
        model = Circle
        fields = ['image','description', 'budget', 'members_num', 'gender_rate', 'alcohol', 'hard', 'practice_date', 'practice_place','twitter_url', 'insta_url', 'line_url']
