from rest_framework.viewsets import ModelViewSet
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer
from .models import ShoppingList, ShoppingListItem


class ShoppingListViewSet(ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ShoppingListItemViewSet(ModelViewSet):
    queryset = ShoppingListItem.objects.all()
    serializer_class = ShoppingListItemSerializer
