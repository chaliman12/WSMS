from django import forms
from django.forms import ModelForm
from .models import *


class UserForm(ModelForm):
    # user_name=forms.EmailField(widget=forms.EmailInput,label='Your Email')
    # pass_word=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','user_name','pass_word','user_type']
        widgets={
             'first_name':forms.TextInput(attrs={'class':"form-control form-control"
                                                 ,'placeholder':'Enter First Name'}),
             'last_name':forms.TextInput(attrs={'class':"form-control form-control",'placeholder':'Enter Last Name' }),
             'user_name':forms.EmailInput(attrs={'class':"form-control form-control",'placeholder':'Enter user Email'}),
             'pass_word':forms.PasswordInput(attrs={'class':"form-control form-control",'placeholder':'Enter user password'}),
             "user_type": forms.Select(attrs={"class": "form-control",'placeholder':'Enter user Email'}),
        }
class UserPermissionsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['view_dashboard', 'view_user', 'view_item', 'view_component', 'view_assignment', 'view_section', 'view_report',
                  'add_user','add_item','add_component','add_assignment','add_section'
                  ,'delete_user','delete_component','delete_section','delete_assignment','delete_item' ]
        widgets = {
        'view_dashboard': forms.CheckboxInput(),
        'view_user': forms.CheckboxInput(),
        'view_item': forms.CheckboxInput(),
        'view_component': forms.CheckboxInput(),
        'view_section': forms.CheckboxInput(),
        'view_assignment': forms.CheckboxInput(),
        'view_report': forms.CheckboxInput(),
        'add_user': forms.CheckboxInput(),
        'add_item': forms.CheckboxInput(),
        'add_component': forms.CheckboxInput(),
        'add_assignment': forms.CheckboxInput(),
        'add_section': forms.CheckboxInput(),
        'delete_user': forms.CheckboxInput(),
        'delete_item': forms.CheckboxInput(),
        'delete_component': forms.CheckboxInput(),
        'delete_section': forms.CheckboxInput(),
        'delete_assignment': forms.CheckboxInput(),
        }
class ItemForm(forms.ModelForm):
    # specify the fields and widgets for the form
    class Meta:
        model = Item
        fields = ["ws_id", "stock_id", "Serial_no", "delivered_by", "received_by", "remark"]
        widgets = {
        "ws_id": forms.TextInput(attrs={"class": "form-control"}),
        "stock_id": forms.TextInput(attrs={"class": "form-control"}),
        "Serial_no": forms.TextInput(attrs={"class": "form-control"}),
        "delivered_by": forms.TextInput(attrs={"class": "form-control"}),
        "received_by": forms.TextInput(attrs={"class": "form-control"}),
        "remark": forms.Textarea(attrs={"class": "form-control"}),
        }
        
            

from django import forms
from django.forms import inlineformset_factory
from .models import Assignments, Component

from django import forms
from django.forms import inlineformset_factory
from .models import Component

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ["stock_id", "Serial_no"]
        widgets = {
            "stock_id": forms.TextInput(attrs={"class": "form-control"}),
            "Serial_no": forms.TextInput(attrs={"class": "form-control"}),
        }

ComponentFormSet = inlineformset_factory(Item, Component, form=ComponentForm, extra=1)


class SectionForm(forms.ModelForm):
    manager = forms.ModelChoiceField(queryset=User.objects.filter(user_type='Manager'
                ,is_active=True), label="Engineer",
                widget=forms.Select(attrs={"class":"form-control"})) 
    class Meta:
        model = Section
        fields = [ "name", "manager"]
        widgets = {
        "name": forms.TextInput(attrs={"class": "form-control"}),
        "manager": forms.Select(attrs={"class": "form-control"}),
        }
        


class AssignmentForm(forms.ModelForm):
    
    engineer = forms.ModelChoiceField(queryset=User.objects.filter(user_type='Engineer'
                ,is_active=True), label="Engineer",
                widget=forms.Select(attrs={"class":"form-control"})) # assume user_type 3 is engineer
    Section = forms.ModelChoiceField(queryset=Section.objects.filter(is_valid=True), 
            label="Section",widget=forms.Select(attrs={"class":"form-control"}))
    class Meta:
        model=Assignments
        fields = ["item", "engineer",'Section',"remark"]
        widgets = {
        "item": forms.HiddenInput(attrs={"class": "form-control"}),
        "engineer":forms.Select(attrs={"class":"form-control"}),
        "Section": forms.Select(attrs={"class": "form-control"}),
        "remark": forms.Textarea(attrs={"class": "form-control"}),
        }





class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','user_name','profile_picture']



from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}),
        label="Old Password"  # Change the label
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
        label="New Password"  # Change the label
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}),
        label="Confirm New Password"  # Change the label
    )

