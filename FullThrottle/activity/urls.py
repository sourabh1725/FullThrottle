"""
Configuring endpoint to fetch the view index
"""
from django.conf.urls import url
from .views import index

urlpatterns = [
    url('', index)
]
