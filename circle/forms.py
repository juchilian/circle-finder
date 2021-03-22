from django import forms

from .models import Circle

class CircleModelForm(forms.ModelForm):
    practice_date = forms.CharField(required=False,label='活動日',widget=forms.TextInput(attrs={
        'placeholder': '例) 平日毎日、月～水 etc...'
    }))
    practice_place = forms.CharField(required=False,label='活動場所',widget=forms.TextInput(attrs={
        'placeholder': '例) 小机、多摩川 etc...'
    }))
    twitter_url = forms.URLField(required=False,widget=forms.URLInput(attrs={
        'placeholder': '例) https://twitter.com/keiotennis'
    }))
    insta_url = forms.URLField(required=False,widget=forms.URLInput(attrs={
        'placeholder': '例) https://www.instagram.com/keiotennis'
    }))
    line_url = forms.URLField(required=False,widget=forms.URLInput(attrs={
        'placeholder': '例) https://line.me/keiotennis'
    }))
    class Meta:
        model = Circle
        fields = ['image','description', 'budget', 'members_num', 'gender_rate', 'alcohol', 'hard', 'experienced', 'event', 'practice_date', 'practice_place','twitter_url', 'insta_url', 'line_url']
