from django.urls import re_path, path
from web.views import index

urlpatterns = [
    path('', index)
]

