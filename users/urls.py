from users import views
from django.urls import path
urlpatterns = [
    path('accounts/register/', views.regester.index, name='register'),

]