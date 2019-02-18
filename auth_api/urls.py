from .api import LoginApiView
from django.urls import path
urlpatterns = [
    path('', LoginApiView.as_view())
]
