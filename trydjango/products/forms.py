from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={
                                   'placeholder':'Type here the title'
                                }
                            ))

    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': 'Description',
                                          'class': 'new-class-name two',
                                          'rows': 20,
                                          'cols': 50
                                      }
                                  ))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError('This is not a valid title')




class RawProductForm(forms.Form):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={
                                   'placeholder':'Type here the title'
                                }
                            ))
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': 'Description',
                                          'class': 'new-class-name two',
                                          'rows': 20,
                                          'cols': 50
                                      }
                                  ))
    price = forms.DecimalField(initial=199.99)
