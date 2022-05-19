# from django.urls import path
# from .views import RegisterUser, LoginUser, logout_user
from django.urls import path
from .import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.index, name='/'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('foods/', views.foods, name='foods'),
    path('order/', views.create, name='order'),
    path('check/', views.check, name='check'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('supplier/', views.supplier, name='supplier'),



    path("register", register_request, name="register"),
    path("login/", login_request, name="login"),
    path('logout/', logout_user, name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)