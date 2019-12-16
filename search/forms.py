from django import forms

class ContactForm(forms.Form):
    producto = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'Nombre del producto'}))


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        producto = cleaned_data.get('producto')
        if not producto:
            raise forms.ValidationError('Llena el campo producto')