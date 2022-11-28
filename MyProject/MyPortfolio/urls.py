from django.urls import path
from MyPortfolio.views import contact, home, about

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]