from django.shortcuts import render
from django.views.generic import CreateView
from product.forms import RegistrationForm, LoginForm, ProductForm, UserEditForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView, TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from product.models import Product
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def signin_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "invalid session")
            return redirect("signin")
        else:
            return fn(request, *args, **kwargs)

    return wrapper


decs = [signin_required, never_cache]


class SignupView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'account created')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'account creation failed')
        return super().form_invalid(form)


class SigninView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('product_list')
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request, username=uname, password=pwd)

            if usr:
                login(request, usr)
                print("hello")
                return redirect("http://127.0.0.1:8000/productlist")
            else:
                messages.error(request, "invalid credentials")
                return render(request, 'login.html', {"form": form})
            
        else:
            print("'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


@method_decorator(decs, name='dispatch')
class HomeView(TemplateView):
    template_name = 'base.html'


@method_decorator(decs, name='dispatch')
class ProductListView(ListView):
    template_name = 'productlist.html'
    context_object_name = 'products'
    model = Product


# @method_decorator(decs, name='dispatch')
class ProductDetailView(DetailView):
    template_name = 'detailview.html'
    context_object_name = 'product'
    pk_url_kwarg = "id"
    model = Product


@method_decorator(decs, name='dispatch')
class ProductAddView(CreateView):
    template_name = 'post_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


# class UserProfile(TemplateView):
#     template_name = "userdisplay.html"


@method_decorator(decs, name='dispatch')
class UserEditView(CreateView):
    template_name = 'user_profile.html'
    form_class = UserEditForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "user details have been updated")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "couldnt update user details")
        return super().form_invalid(form)


def logout_view(request, *args, **kwargs):
    logout(request)
    messages.success(request, "loggedout")
    return redirect('signin')

from .models import UserProfile
def profile_view(request, *args, **kwargs):
    print('*******************************************')
    print(request.user)
    qs = UserProfile.objects.get(user=request.user)
    template_name = "userdisplay.html"
    # return redirect('signin')
    return render(request, 'userdisplay.html', {"qs": qs})








