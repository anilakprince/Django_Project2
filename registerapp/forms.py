from django import forms
from.models import table


class AddForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=table.GENDER_CHOICES, widget=forms.RadioSelect(attrs={'id':'gender'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','id':'confirm_password'}))

    class Meta:
        model=table

        fields=('firstname','lastname','email','phone','password','confirm_password','gender')

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control','id':'firstname'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','id':'lastname'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'email'}),
            'phone':forms.TextInput(attrs={'class':'form-control','id':'phone'}),
            'password':forms.TextInput(attrs={'class':'form-control','id':'password'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'id':'confirm_password'}),
          
           
            
        }