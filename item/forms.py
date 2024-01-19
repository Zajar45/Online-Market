from django import forms
from .models import item

INPUT_CLASSES = 'form-control'

class NewItem(forms.ModelForm):

    class Meta:

        model = item
        fields = ('category', 'name', 'description','price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class':INPUT_CLASSES
                }),

                'name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
                }),
                'description': forms.Textarea(attrs={
                'class':INPUT_CLASSES
                }),

                'price': forms.TextInput(attrs={
                'class':INPUT_CLASSES
                }),

                'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES
                }),
        }

class EditItem(forms.ModelForm):
    
    class Meta:
    
        model = item
        fields = ( 'name', 'description','price', 'image','is_sold')
                
        widgets = {
                'name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
                }),
                
                'description': forms.Textarea(attrs={
                'class':INPUT_CLASSES
                }),
                
                'price': forms.TextInput(attrs={
                'class':INPUT_CLASSES
                }),
                
                'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES
                }),
        }
        