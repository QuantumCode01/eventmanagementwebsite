from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User,event



# form to create user, it inherits the builtin Usercreation form
class UserRegisterationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        # widgets to apply bootsraps form control class to each filed of user registeration form
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            }   
    
# form to authenticate the user when user tries to log in 
class UserAuthenticationForm(AuthenticationForm):
   password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
   username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'})) 
 
# form to create events  
class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ['event_name','date','time','location','image']
        labels={'event_name':"Event Title",'date':'Event Starts','time':'Time','location':'Venue Location','image':'Main Event Image'}
        widgets={'event_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Be clear and descriptive'}), 'date':forms.DateInput(attrs={'type':'date','placeholder':'mm-dd-yyyy','class':'form-control'}),
           'time':forms.TimeInput(attrs={'type':'time','class':'form-control'}),
           'location':forms.TextInput(attrs={'class':'form-control'}),} 