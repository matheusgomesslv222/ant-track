from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from .forms import UsuarioInfoCreationForm, UsuarioInfoChangeForm
from .models import UsuarioInfo


# Create your views here.

def home(request):
    return render(request, 'login.html')

class UserCreateView(CreateView):
    form_class = UsuarioInfoCreationForm
    template_name = 'cadastro.html'
    success_url = reverse_lazy('home')

class UserListView(ListView):
    model = UsuarioInfo
    template_name = 'user_list.html'
    context_object_name = 'users'