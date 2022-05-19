from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm, ProvideForm
from .models import *
from .forms import *


# from django.db import


# class HomepageView(ListView):
#     model = Product
#     context_object_name = 'posts'
#     paginate_by = 4
#     template_name = 'poll/index.html'
#     extra_context = {'title': 'Home'}
#
#     def get_context_data(self, *, object_liss = None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         return context



def index(request):
    return render(request, 'data/index.html')


def about(request):
    return render(request, 'data/about.html', )


def check(request):
    check = Order.objects.order_by('data')
    return render(request, 'data/check.html', {'check': check})


def ingredients(request):
    ingredient = IngredientsForBurger.objects.order_by('ingredients_validity')
    return render(request, 'data/ingredients.html', {'i': ingredient})


def menu(request):
    menu = Food.objects.order_by('-id')[:6]
    return render(request, 'data/menu.html', {'meals': menu})


def kitchen(request):
    kitchen = {
        'client': Clients.objects.all(),
        'provide': Provide.objects.all()
    }
    return render(request, 'data/kitchen.html', kitchen)


def foods(request):
    workers = {
        'Supplier': Suppliers.objects.order_by('supplier_id'),
        'Waiter': Waiter.objects.order_by('waiter_id'),
        'Chef': Chef.objects.order_by('id')
    }
    return render(request, 'data/foods.html', workers)


def order(request):
    return render(request, 'data/order.html')


def create(request):
    error = ''
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kitchen')
        else:
            error = get_object_or_404(PostForm, pk=1)

    data = {
        'form': form,
        'error': error,
        'customer': Clients.objects.all()
    }
    return render(request, 'data/order.html', data)


def supplier(request):
    errors = ''
    forms = ProvideForm()
    if request.method == 'POST':
        form = ProvideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kitchen')
        else:
            errors = 'Форма была неверной'

    datas = {
        'forms': forms,
        'error': errors,

    }
    return render(request, 'data/supplier.html', datas)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="data/registration.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="data/login.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    return redirect('login')
