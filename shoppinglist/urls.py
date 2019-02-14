from .api import ShoppingListViewSet, ShoppingListItemViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register('lists', ShoppingListViewSet)
router.register('items', ShoppingListItemViewSet)

urlpatterns = router.urls
