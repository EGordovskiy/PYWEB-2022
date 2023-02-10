from django.urls import path
from .views import IndexShopView, ViewContact, ViewAbout

app_name = 'home'

urlpatterns = [
    path('', IndexShopView.as_view(), name='index'),
    path('contact/', ViewContact.as_view(), name='contact'),
    path('about/', ViewAbout.as_view(), name='about')
]
