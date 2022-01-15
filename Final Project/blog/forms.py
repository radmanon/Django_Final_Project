
from django import forms
from django.forms import ModelForm, fields
from .models import Post
from ckeditor.widgets import CKEditorWidget

from django import forms 
from .models import Person



class PersonForm(forms.ModelForm): 
    class Meta: 
        model = Person 
        fields = ['title', 'image'] 




class BlogPostForm(ModelForm):

    body = forms.CharField(label="توضیحات", widget=CKEditorWidget())


    class Meta:
        model = Post
        fields = ["title", "body", "category", "image"]

    

    def __init__(self, *args, **kwargs):
       super(BlogPostForm, self).__init__(*args, **kwargs)
       #self.fields['author'].widget.attrs['disabled'] = True
       self.fields['title'].widget.attrs['placeholder'] = "یک عنوان را انتخاب کنید"
       self.fields['title'].widget.attrs['title'] = "enter title"



       for visible in self.visible_fields():
           visible.field.widget.attrs['title'] = ''
           visible.field.widget.attrs['class'] = 'new-class'
