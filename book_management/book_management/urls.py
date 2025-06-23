
from django.contrib import admin
from django.urls import path
from book.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerPage/', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),



    path('', home, name='home'),
    path('addBook/', addBook, name='addBook'),
    path('editBook/', editBook, name='editBook'),
    path('viewBook/', viewBook, name='viewBook'),
    path('deleteBook/', deleteBook, name='deleteBook'),
]
