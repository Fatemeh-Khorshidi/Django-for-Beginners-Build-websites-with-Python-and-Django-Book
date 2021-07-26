from django.urls import path
from .views import FirstHomePage

urlpatterns = [
    path('', FirstHomePage.as_view(), name='home'),

]