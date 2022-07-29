from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from user.models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password', 'phone_no', 'address', 'state', 'city'
        )
