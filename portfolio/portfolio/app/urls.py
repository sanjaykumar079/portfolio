from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('contact',views.contact, name='contact'),
    # path('base',views.base, name='base'),
]
