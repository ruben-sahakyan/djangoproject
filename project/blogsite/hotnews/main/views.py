from re import M
from django.shortcuts import redirect, render
from .models import *
from .forms import NewForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .utlis import *





class Homepage(MyMixin, ListView):
    model = Form
    template_name = 'main/index.html'
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_context = self.get_context()
        return dict(list(context.items()) + list(get_context.items()))




class OneCategory(MyMixin, ListView):
    model = Form
    template_name = 'main/category.html'
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_context = self.get_context()
        return dict(list(context.items()) + list(get_context.items()))

    def get_queryset(self):
        return Form.objects.filter(category_id=self.kwargs['category_id'])




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Good register')
            return redirect('home')
        else:
            messages.error(request, 'Problem')

    else:
        form = UserRegisterForm()

    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('login')


class Oneform(MyMixin, DetailView):
    model = Form
    context_object_name = 'form'
    template_name = 'main/oneform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_context = self.get_context()
        return dict(list(context.items()) + list(get_context.items()))




class AddNew(CreateView):
    form_class = NewForm
    template_name = 'main/addnew.html'
    success_url = reverse_lazy('home')




