# from django.urls import path
# from User.views import  admin
from User.views import  User
# urlpatterns = [
#     path('',admin,name="admin-page"),
#     path('post/', User, name="User-page"),
# ]

from django.urls import path
from User import views

app_name = 'User'

urlpatterns = [
    path('form/', views.User, name='my_form'),
    # ... other URLs for your app
]
