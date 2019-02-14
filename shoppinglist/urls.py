from .api import ShoppingListViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register('shoppinglist', ShoppingListViewSet)


urlpatterns = router.urls
