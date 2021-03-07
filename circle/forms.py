from django import forms

from .models import Circle
class CircleForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class CircleModelForm(forms.ModelForm):
    practice_date = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '例) 平日毎日、月～水 etc...'
    }))
    practice_place = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '例) 小机、多摩川 etc...'
    }))
    twitter_url = forms.URLField(widget=forms.TextInput(attrs={
        'placeholder': '例) https://twitter.com/keiotennis'
    }))
    insta_url = forms.URLField(widget=forms.TextInput(attrs={
        'placeholder': '例) https://www.instagram.com/keiotennis'
    }))
    class Meta:
        model = Circle
        fields = ['image','description', 'budget', 'members_num', 'gender_rate', 'alcohol', 'hard', 'practice_date', 'practice_place','twitter_url', 'insta_url']
    
    # def clean_title(self, *args, **kwargs):
    #     instance = self.instance
    #     title = self.cleaned_data.get('title')
    #     qs = Circle.objects.filter(title__iexact=title)
    #     if instance is not None: # not newly creating
    #         qs = qs.exclude(pk=instance.pk)
    #     if qs.exists():
    #         raise forms.ValidationError("This title has already been used.")
    #     return title