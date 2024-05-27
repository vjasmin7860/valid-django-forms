from django import forms
from app.forms import *
from app.models import *

def valid_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('should not start with a')
def valid_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('check the length of the given string')





class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=20,validators=[valid_for_a,valid_for_len])
  
def valid_for_url(value):
    if value.endswith('.in'):
        raise forms.ValidationError('please check the given urls')
    

def valid_for_len(value):
    if len(value)<6:
        raise forms.ValidationError('please give the length of the value')
class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(validators=[valid_for_len])
    url=forms.URLField(validators=[valid_for_url])
    email=forms.EmailField()
    reemail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    
    def clean(self):
        email=self.cleaned_data['email']
        reemail=self.cleaned_data['reemail']
        if email!=reemail:
            raise forms.ValidationError('please check the emails')
        
    def clean_botcatcher(self):
        cu=self.cleaned_data['botcatcher']
        if len(cu)>0:
            raise forms.ValidationError('bot cs is catched ')


class AccessForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField()
