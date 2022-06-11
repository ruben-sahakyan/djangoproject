from django.urls import path
from main.views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', Homepage.as_view(), name='home'),
    path('category/<int:category_id>/', OneCategory.as_view(), name='category'),
    path('oneform/<int:pk>/', Oneform.as_view(), name ='one new'),
    path('addnew/', AddNew.as_view(), name='add new'),
    path('logout/', log_out, name='logout')
]