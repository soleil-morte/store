from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SuperUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "password2"]