from django import forms

from .models import Circle
class CircleForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class CircleModelForm(forms.ModelForm):
    class Meta:
        model = Circle
        fields = ['image','description', 'twitter_url', 'insta_url']
    
    # def clean_title(self, *args, **kwargs):
    #     instance = self.instance
    #     title = self.cleaned_data.get('title')
    #     qs = Circle.objects.filter(title__iexact=title)
    #     if instance is not None: # not newly creating
    #         qs = qs.exclude(pk=instance.pk)
    #     if qs.exists():
    #         raise forms.ValidationError("This title has already been used.")
    #     return title