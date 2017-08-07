from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'registration/signup.html'
