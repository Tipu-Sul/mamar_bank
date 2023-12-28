from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from. constanats import ACCOUNT_TYPE,GENDER_TYPE
from. models import UserBankAccount,UserAddress

class UserRegisterationForm(UserCreationForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender=forms.ChoiceField(choices=GENDER_TYPE)
    account_type=forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address=forms.CharField()
    city=forms.CharField()
    postal_code=forms.IntegerField()
    country=forms.CharField()
    class Meta:
        model=User
        fields=['username','password1', 'password2', 'first_name','last_name',
                 'email','birth_date','street_address','account_type', 'gender', 'postal_code', 'city', 'country']
    
    def save(self,commit=True):
        our_user=super().save(commit=False)
        if commit==True:
            our_user.save()
            account_type=self.cleaned_data.get('account_type')
            gender=self.cleaned_data.get('gender')
            postal_code=self.cleaned_data.get('postal_code')
            country=self.cleaned_data.get('country')
            birth_date=self.cleaned_data.get('birth_date')
            city=self.cleaned_data.get('city')
            street_address=self.cleaned_data.get('street_address')

            UserAddress.objects.create(
                user=our_user,
                country=country,
                postal_code=postal_code,
                city=city,
                street_address=street_address
            )

            UserBankAccount.objects.create(
                user=our_user,
                birth_date=birth_date,
                gender=gender,
                account_type=account_type,
                account_number=100000+our_user.id
            )
        return our_user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                # 'class':(
                #     'appearance-none block w-full bg-gray-200'
                #     'text-gray-700 border border-gray-200 rounded'
                #     'py-3 px-4 leading-tight focus:outline-none'
                #     'focus:bg-white focus:border-gray-500'
                # )
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
            
class UpdateUserForm(forms.ModelForm):
    birth_date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender=forms.ChoiceField(choices=GENDER_TYPE)
    account_type=forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address=forms.CharField()
    city=forms.CharField()
    postal_code=forms.IntegerField()
    country=forms.CharField()
    class Meta:
        model=User
        fields = ("first_name","last_name","email")

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
        if self.instance:
            try:
                user_account=self.instance.account
                user_address=self.instance.address
            except UserBankAccount.DoesNotExist: 
                user_account=None
                user_address=None
            if user_account:
                self.fields['account_type'].initial=user_account.account_type
                self.fields['gender'].initial=user_account.gender
                self.fields['birth_date'].initial=user_account.birth_date
                self.fields['street_address'].initial=user_address.street_address
                self.fields['city'].initial=user_address.city
                self.fields['postal_code'].initial=user_address.postal_code
                self.fields['country'].initial=user_address.country
    def save(self,commit=True):
        user=super().save(commit=False)
        if commit:
            user.save()
            user_account, created=UserBankAccount.objects.get_or_create(user=user)
            user_address, created=UserAddress.objects.get_or_create(user=user)

            user_account.account_type=self.cleaned_data['account_type']
            user_account.gender=self.cleaned_data['gender']
            user_account.birth_date=self.cleaned_data['birth_date']
            user_account.save()

            user_address.street_address=self.cleaned_data['street_address']
            user_address.city=self.cleaned_data['city']
            user_address.postal_code=self.cleaned_data['postal_code']
            user_address.country=self.cleaned_data['country']
            user_address.save()
        return user


