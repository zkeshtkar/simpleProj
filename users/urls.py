from users import views
from django.urls import path
urlpatterns = [
    path('accounts/register/', views.regester.index, name='register'),
    path('accounts/register/confirm/', views.regester.confirm, name='confirm'),

]